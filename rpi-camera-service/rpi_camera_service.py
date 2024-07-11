from typing_extensions import CapsuleType
import gi

gi.require_version("Gst", "1.0")
from gi.repository import Gst, GObject

from datetime import datetime, timezone
from pydantic import BaseModel


Gst.init(None)


class Resolution(BaseModel):
    Width: int
    Height: int


class CameraParameter(BaseModel):

    Framerate: int = 30

    FileResolution: Resolution = Resolution(Width=1920, Height=1080)
    FileBitrate: int = 1500
    FileSpeedPreset: str = "fast"

    StreamResolution: Resolution = Resolution(Width=854, Height=480)
    StreamBitrate: int = 400

    RtspServerPath: str = "rstp://localhost:8554/vertigo"


class CameraStream:
    def __init__(self, params: CameraParameter = CameraParameter()):
        self.now = datetime.now(timezone.utc).astimezone()
        self._params = params
        self._create_pipeline()

    def _create_pipeline(self):
        self.pipeline = Gst.parse_launch(
            "libcamerasrc name=source ! "
            f"video/x-raw,width={self._params.FileResolution.Width},"
            f"height={self._params.FileResolution.Height},"
            f"framerate={self._params.Framerate} ! "
            "tee name=t ! queue ! "
            f"x264enc bitrate={self._params.FileBitrate} "
            f"speed-preset={self._params.FileSpeedPreset} tune=zerolatency ! "
            f"mp4mux ! filesink location={self.now.isoformat()}.mp4 "
            "t. ! queue ! videoscale ! "
            f"video/x-raw,width={self._params.StreamResolution.Width},"
            f"height={self._params.StreamResolution.Height} ! "
            f"openh264enc bitrate={self._params.StreamBitrate*1000} ! video/x-h264 ! "
            f"rtspclientsink location={self._params.RtspServerPath}"
        )

        # TODO add appsink to timestamp every buffer

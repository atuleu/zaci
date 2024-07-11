from datetime import datetime, timezone
import gi
import signal

gi.require_version("Gst", "1.0")
from gi.repository import GLib, Gst, GObject

from pydantic import BaseModel

Gst.init(None)


def _print_message(msg: Gst.Message):
    if msg.type == Gst.MessageType.ERROR:
        print(msg.src.name, msg.parse_error())
    elif msg.type == Gst.MessageType.EOS:
        print(msg.src.name, "EOS")
    elif msg.type == Gst.MessageType.STATE_CHANGED:
        print(msg.src.name, msg.parse_state_changed())
    elif msg.type == Gst.MessageType.STREAM_STATUS:
        print(msg.src.name, msg.parse_stream_status())
    elif msg.type == Gst.MessageType.PROGRESS:
        print(msg.src.name, msg.parse_progress())
    elif msg.type == Gst.MessageType.LATENCY:
        print(msg.src.name, msg.new_latency)
    else:
        print(msg.src.name, msg.type)
    print("")


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

    RtspServerPath: str = "rtsp://localhost:8554/camera/live"


class CameraStream:
    def __init__(self, params: CameraParameter = CameraParameter(), debug=False):
        self.now = datetime.now(timezone.utc).astimezone()
        self._debug = debug
        self._params = params
        self._create_pipeline()

    def _create_pipeline(self):
        if self._debug is False:
            src = "libcamerasrc name=source"

        else:
            src = "videotestsrc is-live=true name=source"

        self.pipeline = Gst.parse_launch(
            f"{src} !"
            f" video/x-raw,width={self._params.FileResolution.Width},height={self._params.FileResolution.Height},framerate={self._params.Framerate} !"
            " tee name=t ! queue ! x264enc"
            f" bitrate={self._params.FileBitrate} speed-preset={self._params.FileSpeedPreset} tune=zerolatency"
            f" ! mp4mux ! filesink name=mp4sink location={self.now.isoformat()}.mp4 t."
            " ! queue ! videoscale !"
            f" video/x-raw,width={self._params.StreamResolution.Width},height={self._params.StreamResolution.Height} !"
            f" openh264enc bitrate={self._params.StreamBitrate*1000} ! video/x-h264 !"
            f" rtspclientsink location={self._params.RtspServerPath}"
        )

        self.pipeline.set_name("pipeline_" + self.now.isoformat())

        # TODO add appsink to timestamp every buffer

    def run(self):
        if self.pipeline is None:
            raise RuntimeError("pipeline is already done")

        bus = self.pipeline.get_bus()
        if bus is None:
            raise RuntimeError("no bus available? this is annoying")

        loop = GLib.MainLoop()

        def on_message(_, msg: Gst.Message):
            if msg.src.name != self.pipeline.name:
                return
            if msg.type == Gst.MessageType.ERROR:
                err, dbg = msg.parse_error()
                raise RuntimeError(f"Gst Error ({msg.src.name}): {err}\n{dbg}")
            if msg.type == Gst.MessageType.EOS:
                loop.quit()

        bus.add_signal_watch()
        bus.connect("message", on_message)

        print(f"starting pipeline {self.pipeline.name}")
        self.pipeline.set_state(Gst.State.PLAYING)

        try:
            loop.run()
        finally:
            self.pipeline.set_state(Gst.State.NULL)
            del self.pipeline

    def stop(self):
        if self.pipeline is None:
            raise RuntimeError("pipeline is not set")
        print(f"stopping pipeline {self.pipeline.name}")
        self.pipeline.send_event(Gst.Event.new_eos())

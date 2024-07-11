import time

from gi.repository import GLib, GObject
from rpi_camera_service.camera_stream import CameraStream
import threading


s = CameraStream(debug=True)


def stop_in():
    time.sleep(4)
    s.stop()


stop = threading.Thread(target=stop_in)
stop.start()

s.run()

stop.join()

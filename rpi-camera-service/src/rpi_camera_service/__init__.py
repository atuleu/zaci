from typing import Optional
from threading import Thread
from fastapi import FastAPI, HTTPException

from rpi_camera_service.camera_stream import CameraParameter, CameraStream


stream: Optional[CameraStream] = None
streamThread: Optional[Thread] = None

app = FastAPI()


@app.get("/camera")
async def get_camera_settings() -> CameraParameter:
    global stream
    if stream is None:
        raise HTTPException(status_code=404, detail="stream is not started")
    return stream._params


@app.post("/camera")
async def start_camera(params: CameraParameter):
    global stream
    global streamThread
    if stream is not None:
        raise HTTPException(status_code=412, detail="stream is already started")

    try:
        stream = CameraStream(params)
        streamThread = Thread(target=stream.run)
        streamThread.start()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/camera")
async def stop_camera():
    global stream
    global streamThread
    if stream is None or streamThread is None:
        raise HTTPException(status_code=404, detail="stream is not started")

    stream.stop()
    streamThread.join()
    stream = None
    streamThread = None

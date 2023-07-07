import threading

from sensors.data_gathering.camera_depth_gather import CameraDepthGather
from processes.camera_depth import DepthRecognition

from controller import Robot
import cv2 as cv
from time import sleep
from queue import Queue

def prueba():
    robot = Robot()

    camera = robot.getCamera('camera')
    camera.enable(10)

    cv.startWindowThread()
    cv.namedWindow("preview")


    stereo = DepthRecognition()
    camera_gatherer = CameraDepthGather(camera)

    queue  = Queue(0)
    event = threading.Event()
    miThread = threading.Thread(target=process1, kwargs={'queue': queue, 'event': event, 'stereo': stereo, 'camera_gatherer': camera_gatherer})
    miThread.start()

    while robot.step(10) != -1:
        event.set()
        if(not queue.empty()):
            image = queue.get()
            cv.imshow("preview", image)
            cv.waitKey(1)
        #sleep(0.1)
    cv.destroyAllWindows()

def process1(queue: Queue, event: threading.Event, stereo, camera_gatherer):
    while True:
        event.wait()
        data = camera_gatherer.get_data()
        image = stereo.process_data(data)
        color_image = cv.cvtColor(image.astype('uint8'), cv.COLOR_GRAY2BGR)
        queue.put(color_image)
        event.clear()

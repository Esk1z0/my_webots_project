from sensors.data_gathering.idata_gather import IDataGather
from utils.EInputs import EInput
from controller import Camera
from time import sleep
import numpy as np

class CameraDepthGather(IDataGather):

    TIME_INTERVAL = 0.01
    def __init__(self, device: Camera):
        self.__camera = device

    def get_data(self):
        data = [self.__get_image()]
        sleep(self.TIME_INTERVAL)
        data.append(self.__get_image())
        return {EInput.CameraDepth : data, EInput.TimeInterval : self.TIME_INTERVAL}

    def __get_image(self):
        image = self.__camera.getImage()
        data = np.frombuffer(image, np.uint8).reshape((self.__camera.getHeight(), self.__camera.getWidth(), 4))
        return data

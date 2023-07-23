from sensors.data_gathering.idata_gather import IDataGather
from controller import Camera
from time import sleep
from utils.EDevices import EDevices

class CameraGather(IDataGather):

    TIME_INTERVAL = 0.01
    def __init__(self, device: Camera):
        self.__camera = device

    def get_data(self):
        data = [self.__get_image()]
        sleep(self.TIME_INTERVAL)
        data.append(self.__get_image())
        return {EDevices.Camera : data, EDevices.TimeInterval : self.TIME_INTERVAL}

    def __get_image(self):
        image = self.__camera.getImage()
        return image

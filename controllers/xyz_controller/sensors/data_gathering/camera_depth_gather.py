from controllers.xyz_controller.sensors.data_gathering.idata_gather import IDataGather
from controller import Camera
from time import sleep


class CameraDepthGather(IDataGather):

    def __init__(self, device: Camera):
        self.__camera = device

    def get_data(self):
        data = [self.__camera.getImage()]
        sleep(0.1)
        data.append(self.__camera.getImage())
        return data

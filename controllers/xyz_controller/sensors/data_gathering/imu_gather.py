from sensors.data_gathering.idata_gather import IDataGather
from utils.EDevices import EDevices
from controller import InertialUnit
from time import sleep


class IMUGather(IDataGather):

    TimeInterval = 0.01

    def __init__(self, device: InertialUnit):
        self.__imu = device

    def get_data(self):
        data = self.__get_data()
        sleep(self.TIMEINTERVAL)
        data.append(self.__get_data())
        return {EDevices.IMU : data, EDevices.TimeInterval : self.TimeInterval}

    def __get_data(self):
        return self.__imu.getQuaternion()


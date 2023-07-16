from sensors.data_gathering.idata_gather import IDataGather
from controller import DistanceSensor
from time import sleep
from utils.EInputs import EInput


class DistanceGather(IDataGather):

    TIMEINTERVAL = 0.01

    def __init__(self, device: DistanceSensor):
        self.__device = device

    def get_data(self):
        data = self.__get_data()
        sleep(self.TIMEINTERVAL)
        data.append(self.__get_data())
        return {EInput.DistanceSensor : data, EInput.TimeInterval : data}

    def __get_data(self):
        return self.__device.getValue()
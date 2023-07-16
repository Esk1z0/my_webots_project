from sensors.data_gathering.idata_gather import IDataGather
from controller import DistanceSensor


class DistanceGather(IDataGather):

    def __init__(self, device: DistanceSensor):
        self.__device = device

    def get_data(self):
        return self.__device.getValue()
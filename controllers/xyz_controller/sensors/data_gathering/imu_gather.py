from sensors.data_gathering.idata_gather import IDataGather
from controller import InertialUnit
class IMUGather(IDataGather):

    def __init__(self, device: InertialUnit):
        self.__imu = device

    def get_data(self):
        data = self.__imu.getQuaternion()
        return data


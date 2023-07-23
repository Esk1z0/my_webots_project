from processes.iprocess import IProcess
from utils.EInputs import EInput
from utils.EDevices import EDevices


class DistanceProcess(IProcess):

    def process_data(self, data : dict):
        values = data.get(EDevices.DistanceSensor, 0)
        data[EInput.DistanceSensor] = values
        if values != 0:
            diff = self.__difference(values)
            data[EInput.DistanceDifferenceSensor] = diff
        return data

    def __difference(self, data, interval):
        return (data[-1] - data[0])/ interval

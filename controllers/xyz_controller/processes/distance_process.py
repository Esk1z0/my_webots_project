from processes.iprocess import IProcess
from utils.EInputs import EInput


class DistanceProcess(IProcess):

    def process_data(self, data : dict):
        values = data.get(EInput.DistanceSensor, 0)
        interval = data.get(EInput.TimeInterval, 0)
        pos = 0
        diff = 0
        if (values != 0) and (interval != 0):
            pos = values[-1]
            diff = self.__difference(values)
        return {EInput.DistanceSensor : pos, EInput.DistanceDifferenceSensor : diff}

    def __difference(self, data, interval):
        return (data[-1] - data[0])/ interval

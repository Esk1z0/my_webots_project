from processes.iprocess import IProcess


class DistanceProcess(IProcess):

    def process_data(self, data):
        return data
from controllers.xyz_controller.utils.ibatch import IBatch
from controllers.xyz_controller.processes.iprocess import IProcess
from controllers.xyz_controller.sensors.data_gathering.idata_gather import IDataGather
from threading import Thread, Event


class DataHandler(Thread):
    def __init__(self, device, batch: IBatch, process: IProcess, data_gatherer: IDataGather):
        self.__device = device
        self.__batch = batch
        self.__process = process
        self.__data_gatherer = data_gatherer
        self.__stop = Event()
        self.__thread = super().__init__()

    def get_data(self):
        return self.__data_gatherer.get_data()

    def pass_data(self, data):
        self.__batch.enqueue(data)

    def run(self):
        while not self.__stop.is_set():
            print("running still")
            try:
                data = self.get_data()
            except Exception as ex:
                print("No data retrieve")
            else:
                processed_data = self.process_data(data)
                self.pass_data(processed_data)
        print("stopping")

    def process_data(self, data):
        return self.__process.process_data(data)

    def stop(self):
        self.__stop.set()
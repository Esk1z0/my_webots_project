from controller import Camera
from controllers.xyz_controller.utils.ibatch import IBatch
from controllers.xyz_controller.processes.iprocess import IProcess
from threading import Thread, Event


class Camera(Thread):
    def __init__(self, camera: Camera, batch: IBatch, process: IProcess):
        self.__camera = camera
        self.__batch = batch
        self.__process = process
        self.__stop = Event

    def get_image(self):
        return self.__camera.getImage()

    def pass_image(self, data):
        self.__batch.enqueue(data)

    def run(self):
        while not self.__stop.is_set():
            try:
                image = self.get_image()
            except Exception as ex:
                print("No image retrieve")
            else:
                processed_image = self.process_data()
                self.pass_image(processed_image)
        print("stopping")

    def process_data(self, data):
        return self.__process.process_data(data)

    def stop(self):
        self.__stop.set()
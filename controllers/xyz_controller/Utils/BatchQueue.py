import threading

from .IBatch import IBatch
from queue import Queue
from threading import Thread
from time import sleep


class BatchQueue(Thread, IBatch):

    """This class is a queue where it saves the last batch if the receiver doesn't dequeued yet, while deleting the previous ones
        after each time interval to keep the latest info for the receiver"""

    def __int__(self, size: int, interval: int):
        self.__queue = Queue(size)
        self.__interval = interval
        self.__stop = threading.Event()
        super().__init__(target=self.run())
        #self.start()

    def __init__(self):
        self.__queue = Queue(2)
        self.__interval = 0.1
        self.__stop = threading.Event()
        self.__thread = super().__init__()

    def run(self):
        print("running")
        while not self.__stop.is_set():
            print("still running")
            sleep(self.__interval)
            if self.__queue.qsize() > 1:
                print("q>1")
                self.__queue.get()
        print("end")

    def stop(self):
        print("stopping")
        self.__stop.set()

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        self.__interval = value

    def dequeue(self):
        return self.__queue.get()

    def enqueue(self, item):
        self.__queue.put(item)

    def qsize(self):
        return self.__queue.qsize()

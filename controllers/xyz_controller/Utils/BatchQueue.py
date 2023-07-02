from .IBatch import IBatch
from queue import Queue
from threading import Thread
from time import sleep


class BatchQueue(Thread, IBatch):

    """This class is a queue where it saves the last batch if the receiver doesn't dequeued yet, while deleting the previous ones
        after each time interval to keep the latest info for the receiver"""

    def __int__(self, size: int, interval: int):
        super().__init__(self, target=self.run())
        self.__queue = Queue(size)
        self.__interval = interval
    def __init__(self):
        self.__queue = Queue(1)
        self.__interval = 0
        super().__init__(self, target=self.run())

    def run(self):
        while True:
            sleep(self.__interval)
            if self.__queue.qsize() > 1:
                self.__queue.get()

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

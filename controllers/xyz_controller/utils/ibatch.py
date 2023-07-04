from abc import ABC
from abc import abstractmethod


class IBatch(ABC):
    """This class is an interface where info is enqueue and dequeue to pass info between the components.

        it's just a queue with extra shit"""

    #@abstractmethod
    #def __int__(self, size: int, interval: int):
    #    pass

    @property
    @abstractmethod
    def interval(self):
        pass

    @interval.setter
    @abstractmethod
    def interval(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

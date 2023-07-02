from abc import ABC
from abc import abstractmethod


class IBatch(ABC):
    """This class is an interface where info is enqueue and dequeue to pass info between the components.

        The idea is that it saves the last batch if the receiver doesn't dequeued yet, while deleting the previous ones
        after each time interval to keep the latest info for the receiver"""

    @abstractmethod
    def __int__(self, size: int, interval: int):
        pass

    @abstractmethod
    @property
    def interval(self):
        pass

    @abstractmethod
    @interval.setter
    def interval(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

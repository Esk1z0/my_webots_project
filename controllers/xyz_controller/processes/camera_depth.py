import numpy

from processes.iprocess import IProcess
from cv2 import cvtColor, rotate, StereoBM,convertScaleAbs, ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE, COLOR_BGR2GRAY
from numpy import maximum
import cv2 as cv

class DepthRecognition(IProcess):
    """The data must come as a numpy array"""

    NUM_DISPARITIES = 80
    BLOCKSIZE = 27

    def process_data(self, data: list) -> numpy.ndarray:
        data = DepthRecognition.pair_func(data, DepthRecognition.grayscale) #first we pass it to grayscale
        rotated_data = DepthRecognition.pair_func(data.copy(), DepthRecognition.rotate90counter) #we rotate 90 degrees for vertical stereo

        image1 = DepthRecognition.depth(data[0], data[1])
        image2 = DepthRecognition.depth(rotated_data[0], rotated_data[1])
        image2 = DepthRecognition.rotate90counter(image2)

        return DepthRecognition.mix(image1, image2)

    @staticmethod
    def pair_func(data, func):
        return [func(data[0]), func(data[1])]

    @staticmethod
    def grayscale(image):
        image = convertScaleAbs(image)
        return cvtColor(image, COLOR_BGR2GRAY)

    @staticmethod
    def rotate90(image):
        return rotate(image, ROTATE_90_CLOCKWISE)

    @staticmethod
    def rotate90counter(image):
        return rotate(image, ROTATE_90_COUNTERCLOCKWISE)

    @staticmethod
    def create_stereoBM():
        return StereoBM.create(DepthRecognition.NUM_DISPARITIES, DepthRecognition.BLOCKSIZE)


    @staticmethod
    def depth(image1, image2):
        stereo = DepthRecognition.create_stereoBM()
        return stereo.compute(image1, image2)

    @staticmethod
    def mix(image1, image2):
        return maximum(image1, image2)

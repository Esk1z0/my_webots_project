import numpy
from utils.EInputs import EInput
from processes.iprocess import IProcess
from cv2 import cvtColor, rotate, StereoBM,convertScaleAbs, ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE, COLOR_BGR2GRAY
from numpy import maximum
import numpy as np

class DepthRecognition(IProcess):
    """The data must come as a numpy array"""

    NUM_DISPARITIES = 16#80
    BLOCKSIZE = 89#27

    def __init__(self):
        self.__stereoBM = self.create_stereoBM()

    def process_data(self, data: dict) -> numpy.ndarray:
        values = data.get(EInput.CameraDepth, 0)
        if values != 0:
            values = self.pair_func(values, self.__preprocess)
            data = self.pair_func(values, self.grayscale) #first we pass it to grayscale
            rotated_data = self.pair_func(data.copy(), self.rotate90) #we rotate 90 degrees for vertical stereo

            image1 = self.depth(data[0], data[1])
            image2 = self.depth(rotated_data[0], rotated_data[1])
            image2 = self.rotate90counter(image2)

            data = self.mix(image1, image2)

        return {EInput.CameraDepth : data}


    def __preprocess(self, image):
        data = np.frombuffer(image, np.uint8).reshape((self.__camera.getHeight(), self.__camera.getWidth(), 4))
        return data

    def pair_func(self, data, func):
        return [func(data[0]), func(data[1])]

    def grayscale(self, image):
        image = convertScaleAbs(image)
        return cvtColor(image, COLOR_BGR2GRAY)

    def rotate90(self, image):
        return rotate(image, ROTATE_90_CLOCKWISE)

    def rotate90counter(self, image):
        return rotate(image, ROTATE_90_COUNTERCLOCKWISE)

    def create_stereoBM(self):
        return StereoBM.create(DepthRecognition.NUM_DISPARITIES, DepthRecognition.BLOCKSIZE)



    def depth(self, image1, image2):
        return self.__stereoBM.compute(image1, image2)

    def mix(self, image1, image2):
        return maximum(image1, image2)

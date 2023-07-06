import unittest
from controllers.xyz_controller.processes.camera_depth import DepthRecognition
import cv2 as cv
import matplotlib.pyplot as plt
from timeit import timeit

class MyTestCase(unittest.TestCase):
    DIR_IMAGE1 = '/Users/jeste/Pictures/Screenshots/my_frst_webots_world_2.png'
    DIR_IMAGE2 = '/Users/jeste/Pictures/Screenshots/my_frst_webots_world_3.png'

    def test_grayscale(self):
        im1 = cv.imread(MyTestCase.DIR_IMAGE1)
        plt.imshow(DepthRecognition.grayscale(im1), cmap='gray')
        plt.show()
        self.assertEqual(True, True)
    def test_rotate(self):
        im1 = cv.imread(MyTestCase.DIR_IMAGE1)
        im1 = DepthRecognition.rotate90(im1)

        plt.imshow(DepthRecognition.grayscale(im1), cmap='gray')
        plt.show()
        self.assertEqual(True, True)

    def test_rotate_counter(self):
        im1 = cv.imread(MyTestCase.DIR_IMAGE1)
        im1 = DepthRecognition.rotate90(im1)
        im1 = DepthRecognition.rotate90counter(im1)
        plt.imshow(DepthRecognition.grayscale(im1), cmap='gray')
        plt.show()
        self.assertEqual(True, True)

    def test_depth(self):
        im1 = cv.imread(MyTestCase.DIR_IMAGE1)
        im2 = cv.imread(MyTestCase.DIR_IMAGE2)
        im1 = DepthRecognition.grayscale(im1)
        im2 = DepthRecognition.grayscale(im2)



        image = DepthRecognition.depth(im1, im2)

        plt.imshow(image, cmap='gray')
        plt.show()
        self.assertEqual(True, True)

    def test_full_process(self):
        im1 = cv.imread(MyTestCase.DIR_IMAGE1)
        im2 = cv.imread(MyTestCase.DIR_IMAGE2)

        process = DepthRecognition()

        image = process.process_data([im1, im2])

        plt.imshow(image)
        plt.show()
        self.assertEqual(True, True)

    def test_time_comsupmtion(self):
        im1 = cv.imread(MyTestCase.DIR_IMAGE1)
        im2 = cv.imread(MyTestCase.DIR_IMAGE2)

        process = DepthRecognition()

        def func():
            process.process_data([im1, im2])

        time = timeit(func, number=100)
        print(time/100)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()

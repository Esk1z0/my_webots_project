import unittest
from PIL import Image
from keras.applications import EfficientNetV2B0
from keras.applications.efficientnet import decode_predictions
import numpy as np
from time import time
import tensorflow as tf


class MyTestCase(unittest.TestCase):

    DIR_IMAGE1 = '/Users/jeste/Documents/chanclas_meme.jpg'
    DIR_IMAGE2 = "/Users/jeste/Documents/water-gbc7ef3d8d_640.jpg"
    DIR_IMAGE3 = "/Users/jeste/Documents/portrait-g32afaf6bf_640.jpg"

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_process(self):
        tf.config.set_visible_devices([], 'GPU')
        model = EfficientNetV2B0()
        image = Image.open(MyTestCase.DIR_IMAGE3, mode='r')

        target_size = (224, 224)
        initial_time = time()
        image = image.resize(target_size)
        x = np.array(image)
        x = np.expand_dims(x, axis=0)



        preds = model.predict(x)
        final_time = time()
        print("\nTiempo: ", final_time-initial_time)
        decoded_preds = decode_predictions(preds, top=5)[0]
        for label, description, probability in decoded_preds:
            print(f'{description}: {probability}')
        print("\n", decoded_preds)

        image.close()
        self.assertEqual(True, True)


    def test_objeto(self):

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

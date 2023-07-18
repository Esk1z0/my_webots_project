from iprocess import IProcess
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np

class CameraRecognitionProcess(IProcess):

    def process_data(self, data) -> dict:
        pass

    def __get_model(self):
        model = VGG16(weights='imagenet')
        return model

    def __preprocess(self, img):
        x = np.expand_dims(img, axis=0)
        x = preprocess_input(x)
        return x

    def __predict(self, data, model):
        preds = model.predict(data)
        return preds

    def __decode_prediction(self, preds):
        decoded_preds = decode_predictions(preds, top=3)[0]
        return decoded_preds
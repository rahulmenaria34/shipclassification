import numpy as np
from PIL import Image
import cv2
import tensorflow as tf
from tensorflow import keras

class traffic:
    def __init__(self,filename):
        self.filename =filename


    def trafficsign(self):
        class_dict = {'1': 'Cargo', '2': 'Military', '3': 'Carrier', '4': 'Cruise', '5': 'Tankers'}

        model_path = "C:\\Users\\Kishan\\Desktop\\Traffic_sign_classfication-main\\Traffic_sign_classfication-main\\ship_classifier.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        imagename = self.filename
        image = cv2.imread(imagename)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((224, 224))
        expand_input = np.expand_dims(resize_image,axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        pred = loaded_model.predict(input_data)
        result =class_dict.get(str(np.argmax(pred, axis = -1)[0]+1))
        #print(result)
        return [{"image": result}]

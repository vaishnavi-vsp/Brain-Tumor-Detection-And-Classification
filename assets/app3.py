
import numpy as np
import cv2
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from PIL import Image
from matplotlib.pyplot import imshow
import os

model = keras.models.load_model("new/classification.h5")


img = Image.open('Training/meningioma_tumor/m (3).jpg')

classes = os.listdir('Training')

def names(number):
    if(number == 0):
        return classes[2]
    elif(number == 1):
        return classes[3]
    elif(number == 2):
        return classes[1]
    elif(number == 3):
        return classes[0]

dim = (150,150)
x = np.array(img.resize(dim))
x = x.reshape(1,150,150,3)
answ = model.predict_on_batch(x)
classification = np.where(answ == np.amax(answ))[1][0]  
imshow(img)
print(str(answ[0][classification]*100) + '% Confidence This Is ' + names(classification))

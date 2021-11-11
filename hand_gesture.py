import cv2
import numpy as np
from segment import segment
import os
import h5py
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D,MaxPooling2D,Activation, Dropout, Flatten, Dense, BatchNormalization
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

cap = cv2.VideoCapture(0)

fps = int(cap.get(cv2.CAP_PROP_FPS))
model = keras.Sequential(
    [
        layers.Input((32, 32, 1)),
        layers.Conv2D(512, 3, padding="same",activation='relu'),
        layers.Conv2D(256, 3, padding="same",activation='relu'),
        layers.Conv2D(128, 3, padding="same",activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(6,activation='softmax'),
    ]
)
model.load_weights('my_model_weights.h5')
while cap.isOpened():
    ret, frame = cap.read()
    cropped_frame = frame[100:400, 100:300]
    cropped_frame=cv2.cvtColor(cropped_frame,cv2.COLOR_BGR2GRAY)
    thres,seg = segment(cropped_frame)
    cv2.imshow('Captured Frame', thres)
    thres=cv2.resize(thres,(32,32))
    thres=np.reshape(thres,(1,32,32,1))
    dic={}
    dic[0]='blank'
    dic[1]='fist'
    dic[3]='super'
    dic[4]='thumbsdown'
    dic[5]='thumbsup'
    dic[2]='five'
    print(dic[np.argmax(model.predict(thres))])
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    image = cv2.putText(cropped_frame,dic[np.argmax(model.predict(thres))], org, font,
                   fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('frame',frame)
    cv2.imshow('cropped',image)
    if cv2.waitKey(1) == ord('q'):
        break

    keypress = cv2.waitKey(1) & 0xFF

cap.release()
cv2.destroyAllWindows()

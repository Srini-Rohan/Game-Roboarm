import rospy
import cv2
import numpy as np
from segment import segment
import numpy as np

from keras.models import Sequential
from tensorflow import keras
from tensorflow.keras import layers


cap = cv2.VideoCapture(0)

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

model.load_weights('/home/srinir/catkin_ws/src/HardWired/control/src/my_model_weights.h5')
while cap.isOpened():
    ret, frame = cap.read()
    cropped_frame = frame[100:400, 100:300]
    cropped_frame=cv2.cvtColor(cropped_frame,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('bg.jpg',cropped_frame)
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
    ans=np.argmax(model.predict(thres))
    print(dic[ans])
    file=open("gesture.txt",'w')
    file.write(str(ans))
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    image = cv2.putText(frame,dic[ans], org, font,
                   fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('frame',frame)#$
    cv2.imshow('cropped',cropped_frame)
    if cv2.waitKey(1) == ord('q'):
        break

    keypress = cv2.waitKey(1) & 0xFF

cap.release()
cv2.destroyAllWindows()


import cv2
import numpy as np
from hand_mask import hand_gesture

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

while True:
    ret, frame = cap.read()

    cropped_frame, masking, gray = hand_gesture(frame)

    cv2.imshow("Original_frame", frame)
    cv2.imshow("Masking", masking)

    '''
    Approach->  The white pixels in the mask corresponds to the hand.
    We will fing the white pixels with highest white co-ordinates.
    If the highest 'y' is increasing that means the motion is upward.
    If it is decreasing then it is downwards.
    '''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # print(masking)
cap.release()
cv2.destroyAllWindow()
















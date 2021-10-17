import cv2
import numpy as np

def hand_gesture(frame):
    # here frame will will be the fees from the video frame.

    cropped_frame = frame[100:400, 100:300]  # trying to take only the hand part.
    dup_cropped = frame[100:400, 100:300]
    
    gray = cv2.cvtColor(dup_cropped, cv2.COLOR_BGR2LAB)

    lower_color = np.array([40, 120, 120], dtype=np.uint8)
    upper_color = np.array([255, 170, 170], dtype=np.uint8)

    masking = cv2.inRange(gray, lower_color, upper_color)

    # cv2.imshow("Original_frame", frame)
    # cv2.imshow("Cropped_frame", cropped_frame)
    # cv2.imshow("Masking", masking)

    return [cropped_frame, masking]

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

while True:
    ret, frame = cap.read()

    cropped_frame, masking = hand_gesture(frame)

    cv2.imshow("Original_frame", frame)
    cv2.imshow("Cropped_frame", cropped_frame)
    cv2.imshow("Masking", masking)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # print(masking)
cap.release()
cv2.destroyAllWindow()


    
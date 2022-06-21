import cv2
import numpy as np

bg=cv2.imread('bg.jpg',0)

def segment(image, threshold=25):
    global bg
    diff = cv2.absdiff(bg.astype("uint8"), image)
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
    (cnts, _) = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 0:
        return (thresholded,thresholded)
    else:
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)

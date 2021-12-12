import cv2
import numpy as np

import cv2
import sys

vid_capture = cv2.VideoCapture("http://192.168.29.69:4747/video")
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))

size = (frame_width, frame_height)
result = cv2.VideoWriter('bot_top_camera.mp4',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         25, size)
if (vid_capture.isOpened() == False):
	print("Error opening the video file")


params = cv2.SimpleBlobDetector_Params()
params.filterByInertia
params.minInertiaRatio = 0.6

detector = cv2.SimpleBlobDetector_create(params)

def get_blobs(frame):
    blur = cv2.medianBlur(frame, 7)
    grayscale = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    blobs = detector.detect(grayscale)

    return blobs

def get_number(blobs):
    X = []
    for b in blobs:
        pos = b.pt
        if pos != None:
            X.append(pos)
    X = np.array(X)
    print(len(X))
    a=len(X)
    if len(X)>0:
        sum_x=0
        sum_y=0
        for i in range(len(X)):
            sum_x+=X[i][0]
            sum_y+=X[i][1]
        return [a, sum_x/a,sum_y/a]
    else:
        return [0,0,0]
def display_info(frame, data, blobs):
    for b in blobs:
        pos = b.pt
        r = b.size / 2
        cv2.circle(frame, (int(pos[0]), int(pos[1])),
                   int(r), (255, 0, 0), 2)
    image = cv2.putText(frame,str(data[0]),(int(data[1]),int(data[2])), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 0),2, cv2.LINE_AA)


while(vid_capture.isOpened()):

    ret, frame = vid_capture.read()

    blobs = get_blobs(frame)
    data = get_number(blobs)
    file=open("dice.txt",'w')
    file.write(str(data[0]))
    display_info(frame, data, blobs)

    cv2.imshow("frame", frame)
    res = cv2.waitKey(1)
    if res & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

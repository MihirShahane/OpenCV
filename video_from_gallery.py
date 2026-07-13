# In this file a downloaded video from this device is played.

print("Hello World")

import cv2 as cv
import sys

video_path = "C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_1.mp4"

source = cv.VideoCapture(video_path)
win_name = 'Downloaded video'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while cv.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv.imshow(win_name,frame)

cv.destroyWindow(win_name)
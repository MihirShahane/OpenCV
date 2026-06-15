# This file gives some basic image annotation techniques.

import cv2 as cv
import numpy as np

print("Hello World")

img1=cv.imread(r"C:\myprogsPY\OpenCV\apollo_launch.png")
"""print("Image size is ",img1.shape)"""  # Output is-(392,697,3)

# Drawing a line-

img1_copy=img1.copy()
"""cv.line(img1_copy,(25,25),(100,100),(0,255,0),2)
cv.imshow('Image1',img1_copy)
cv.waitKey(0)""" # Draws a line from (25,25) to (100,100) of Green color with thickness 2.

# Drawing a circle(filled and unfilled)-

"""cv.circle(img1_copy,(100,100),20,(255,0,0),3) 
cv.circle(img1_copy,(200,200),20,(255,0,0),-1)
cv.imshow('Circle',img1_copy)
cv.waitKey(0)""" # For a filled circle the thickness has to be '-1'.

# Drawing a rectangle-

"""cv.rectangle(img1_copy,(100,300),(200,500),(0,0,255),2)
cv.imshow('Rectangle',img1_copy)
cv.waitKey(0)"""

# Adding text to the image-

"""text="Apollo 11 Saturn V launch,July 1969"
fontscale=2.3
fontface=cv.FONT_HERSHEY_PLAIN
fontthickness=2
fontcolor=(0,255,0)
cv.putText(img1_copy,text,(00,100),fontface,fontscale,fontcolor,fontthickness,cv.LINE_AA)
cv.imshow('Annotated',img1_copy)
cv.waitKey(0)"""
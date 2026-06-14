# This file gives intro to OpenCV.
print("Hello World")
import cv2 as cv
import numpy as np

# OpenCV stores image in the BGR format.

# Displaying an image-

img=cv.imread(r"C:\Users\Mihir\Downloads\checkered.jpg") # Always give path of the image.
"""cv.imshow('Image',img)
cv.waitKey(0)"""

"""print("Image size is ",img.shape) 
print("Data type of image is ",img.dtype)"""

img2=cv.imread(r"C:\myprogsPY\OpenCV\coca_cola.png")
"""cv.imshow('Image1',img2)
cv.waitKey(0)"""

# Displaying a color image as gray scale image-

img3=cv.imread(r"C:\myprogsPY\OpenCV\coca_cola.png")
gray_img3=cv.cvtColor(img3,cv.COLOR_BGR2GRAY)
"""cv.imshow('Image1',gray_img3)
cv.waitKey(0)"""

# Splitting color channels-

img4=cv.imread(r"C:\myprogsPY\OpenCV\scenery.webp")
b,g,r=cv.split(img4)
"""cv.imshow('Blue Channel', b)
cv.imshow('Green Channel', g)
cv.imshow('Red Channel', r)
cv.waitKey(0)""" # Gives image as grayscale and brighter spots indicate more of the color.  

# Merge back to original
merged = cv.merge([b,g,r]) # Gives back the original image as it was.
"""cv.imshow('Merged', merged)
cv.waitKey(0)"""

# Converting colorspaces-

img5=cv.imread(r"C:\myprogsPY\OpenCV\NZ_Scenery.png")
# BGR to RGB and back-
rgb=cv.cvtColor(img5,cv.COLOR_BGR2RGB)
bgr=cv.cvtColor(img5,cv.COLOR_RGB2BGR)
# BGR to Grayscale-
gray=cv.cvtColor(bgr,cv.COLOR_BGR2GRAY)
# BGR to HSV-
hsv=cv.cvtColor(bgr,cv.COLOR_BGR2HSV)
# BGR to HLS-
hls=cv.cvtColor(bgr,cv.COLOR_BGR2HLS)
# BGR to LAB-
lab=cv.cvtColor(bgr,cv.COLOR_BGR2LAB) 
  


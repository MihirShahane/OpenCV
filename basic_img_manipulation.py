# This file gives some basic image manipulation techniques.

import cv2 as cv
import numpy as np

print("Hello World")

img1=cv.imread(r"C:\myprogsPY\OpenCV\checkered.png",0)  # The "0" at the end tells that the image loads in grayscale.
"""cv.imshow('Image',img1)
cv.waitKey(0)"""

# Accessing individual pixel of an image-

"""pixel=img1[0,0]
print(pixel)""" # Since our image is a grayscale image the 'pixel' here prints the intensity of that particular pixel.abs

img_bgr=cv.cvtColor(img1,cv.COLOR_GRAY2BGR)
"""pixel=img_bgr[0,0]
print(pixel)""" # For a BGR image as 'img_bgr' the 'pixel' here prints the triplt [B,G,R] where each value shows intensity of that color.

# Modifying pixels of an image-

img1_copy=img1.copy() # Creates a copy of that image, necessary when modifying the pixels so that original image doesnt change.
"""img1_copy[0,0]=0
img1_copy[4,4]=0
img1_copy[8,8]=0 
cv.imshow('Image1',img1_copy)
cv.waitKey(0)""" # Sets the intensity of the 3 pixels mentioned to 0 (pure Black).

# Modifying region of pixels-

"""img1_copy[100:200,200:300]=0
cv.imshow('Image1',img1_copy)
cv.waitKey(0)"""  # Entire region mentioned above gets converted to 'black' color.

# Cropping images-

img2=cv.imread(r"C:\myprogsPY\OpenCV\NZ_Boat.png")
"""print("Image size ",img2.shape)""" # Output-(326,493,3)

cropped=img2[81:244,123:369]
"""cv.imshow("Original",img2)
cv.imshow("Cropped",cropped)
cv.waitKey(0)"""  # Cropping of image is obtained by simple array slicing.

# Resizing images-

# 1.Resize to specific dimensions-
img2_copy=img2.copy()

"""resized=cv.resize(img2_copy,(400,250)) # Takes width of the image(rows) first then heigth of the image(columns).
cv.imshow("Resized",resized)
cv.imshow("Original",img2_copy)
cv.waitKey(0)""" # Changes size to (250,400,3).

# 2.Specifying scaling factor-

"""half=cv.resize(img2_copy,(0,0),fx=0.5,fy=0.5)
double=cv.resize(img2_copy,(0,0),fx=2,fy=2)
cv.imshow("Half",half)
cv.imshow("Double",double)
cv.imshow("Original",img2_copy)
cv.waitKey(0)""" # The (0,0) in resize function here tells OpenCV to simply ignore the destination size(dsize) parameter required in resize function.

"""What is interpolation-
    When an image is resized,pixels need to be added or removed.Interpolation is the mathematical method that determines what is the value of those pixels."""

# Flipping images-

flipped_x=cv.flip(img2_copy,1)
flipped_y=cv.flip(img2_copy,0)
flipped_both=cv.flip(img2_copy,-1)
"""cv.imshow("Flip_X",flipped_x)
cv.imshow("Flip_Y",flipped_y)
cv.imshow("Flip_Both",flipped_both)
cv.imshow("Original",img2_copy)
cv.waitKey(0)"""  # For the flip function,the flipcodes decide how the image flips.

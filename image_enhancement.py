# This file gives some basic image enhancement techniques.

import cv2 as cv
import numpy as np

print("Hello World")

img1=cv.imread(r"C:\myprogsPY\OpenCV\NZ_Coast.jpg")

# Addition or brightness-

"""matrix=np.ones(img1.shape,dtype='uint8')*50
brighter=cv.add(img1.copy(),matrix)
darker=cv.subtract(img1.copy(),matrix)
cv.imshow('Original',img1)
cv.imshow('Brighter',brighter)
cv.imshow('Darker',darker)
cv.waitKey(0)""" # The matrix defined here is a NumPy array with same dimensions as that of the original image.All the elements of that array have intensity set to 50.

# Multiplication or Contrast-

# Contrast is essentially how spread out brightness values are across an image,from the darkest to the brightest pixel.Its not a single number stored anywhere.
matrix1=np.ones(img1.copy().shape)*0.8
matrix2=np.ones(img1.copy().shape)*1.2

"""darker=np.uint8(cv.multiply(np.float64(img1.copy()),matrix1))
brighter=np.uint8(cv.multiply(np.float64(img1.copy()),matrix2))
cv.imshow('Original',img1)
cv.imshow('Brighter',brighter)
cv.imshow('Darker',darker)
cv.waitKey(0)""" # The problem with this code is overflow.To fix it we use a function np.clip()

"""lower=np.uint8(cv.multiply(np.float64(img1.copy()),matrix1))
higher=np.uint8(np.clip(cv.multiply(np.float64(img1.copy()),matrix2), 0, 255))
cv.imshow('Original',img1)
cv.imshow('Brighter',lower)
cv.imshow('Darker',higher)
cv.waitKey(0)"""  # Very weird code.

# Image thresholding-
# Thresholding converts a grayscale image into a binary(black and white) image by comparing each pixel to a threshold value and then separating them.

copy=img1.copy()
gray=cv.cvtColor(copy,cv.COLOR_BGR2GRAY)
"""threshold_val=127
max_val=255

ret,thresh=cv.threshold(gray,threshold_val,max_val,cv.THRESH_BINARY)
cv.imshow('Original',gray)
cv.imshow('Thresholded',thresh)
cv.waitKey(0)"""

# Otsu's method- Calculates the optimum value for threshold based on the image's histogram.

"""ret,otsu_thresh=cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print("Otsu calculated threshold value is ",ret)
cv.imshow('Original',gray)
cv.imshow('Otsu Thresholded',otsu_thresh)
cv.waitKey(0)"""

# Adaptive thresholding- Sets different threshold values for different parts of the image based upon the lighting at that part of the image.

"""adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,blockSize=9,C=1)
cv.imshow("Adaptive Thresholded",adaptive_thresh)
cv.waitKey(0)""" # blckSize is the size of the neighbourhood used to calculate threshold value for a certain pixel(it has to be odd).
                 # C value is the constant subtracyed from the calculated mean/weighted mean.

# Bitwise operations on images-



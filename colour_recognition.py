import cv2
import numpy as np
from cv2 import Mat
from numpy import ndarray, dtype, generic
from typing import Any

img = cv2.imread("images/cube_1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# where() function to find the indices of the pixels that match the color range
row_indices, col_indices = np.where(mask == 255)
print(row_indices)
print(col_indices)

# Get the pixel value at the first location where the mask is 255
pixel = img[row_indices[0], col_indices[0]]

# Convert the pixel value from BGR to HSV
hsv_pixel: Mat | ndarray[Any, dtype[generic]] | ndarray = cv2.cvtColor(pixel.reshape(1, 1, 3), cv2.COLOR_BGR2HSV)
print(hsv_pixel)

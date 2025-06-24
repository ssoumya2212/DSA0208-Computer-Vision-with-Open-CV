# Morphological Dilation using OpenCV
import cv2
import numpy as np

img = cv2.imread('input.jpg', 0)
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite('dilation.jpg', dilation)

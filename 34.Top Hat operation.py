# Top Hat operation using OpenCV
import cv2
import numpy as np

img = cv2.imread('input.jpg', 0)
kernel = np.ones((5,5), np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imwrite('tophat.jpg', tophat)

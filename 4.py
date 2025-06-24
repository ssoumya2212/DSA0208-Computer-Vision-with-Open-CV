import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)  # Load in grayscale
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Original Image', cv2.resize(img, (500, 400)))
cv2.imshow('Dilated Image', cv2.resize(dilated, (500, 400)))
cv2.waitKey(0)
cv2.destroyAllWindows()

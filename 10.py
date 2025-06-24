import cv2
import numpy as np

img = cv2.imread('image.jpg')
(h, w) = img.shape[:2]

# Move 100 right, 50 down
M = np.float32([[1, 0, 100], [0, 1, 50]])
translated = cv2.warpAffine(img, M, (w, h))

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Translated', cv2.WINDOW_NORMAL)

cv2.imshow('Original', img)
cv2.imshow('Translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

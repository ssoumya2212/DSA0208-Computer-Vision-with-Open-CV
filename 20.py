import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)

# Laplacian sharpening kernel with negative center
laplacian_kernel = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])

# Apply kernel using filter2D
sharpened = cv2.filter2D(img, -1, laplacian_kernel)

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Sharpened Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

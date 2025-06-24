import cv2
import numpy as np

# Load grayscale image
img = cv2.imread('image.jpg', 0)

# Apply Sobel filter along X axis
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Convert to absolute values and scale to 8-bit
sobelx_abs = cv2.convertScaleAbs(sobelx)

cv2.namedWindow('Sobel X Edge Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Sobel X Edge Detection', sobelx_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()

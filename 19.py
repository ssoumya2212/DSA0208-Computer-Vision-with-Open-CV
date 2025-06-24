import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)

# Apply Sobel in X and Y
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute scale
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# Combine both directions
sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

cv2.namedWindow('Sobel XY Edge Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Sobel XY Edge Detection', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

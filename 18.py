import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)

# Apply Sobel operator along Y axis
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute and then 8-bit
sobely_abs = cv2.convertScaleAbs(sobely)

cv2.namedWindow('Sobel Y Edge Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Sobel Y Edge Detection', sobely_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()

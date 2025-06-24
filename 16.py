import cv2
import numpy as np

# Read grayscale image
img = cv2.imread('image.jpg', 0)

# Compute median pixel intensity
median_val = np.median(img)

# Set thresholds based on median (auto-adjusting)
lower = int(max(0, 0.66 * median_val))
upper = int(min(255, 1.33 * median_val))

edges = cv2.Canny(img, lower, upper)

cv2.namedWindow('Canny Edge Detection', cv2.WINDOW_NORMAL)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

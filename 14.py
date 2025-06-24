import cv2
import numpy as np

# Read the image
img = cv2.imread('image.jpg')
rows, cols = img.shape[:2]

# Source points (4 corners)
pts_src = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])

# Destination points (shifted)
pts_dst = np.float32([[50, 50], [cols - 100, 50], [50, rows - 100], [cols - 100, rows - 100]])

# Compute homography
H, _ = cv2.findHomography(pts_src, pts_dst)

# Apply perspective warp
warped = cv2.warpPerspective(img, H, (cols, rows))

# Show without zooming
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Homography', cv2.WINDOW_NORMAL)

cv2.imshow('Original', img)
cv2.imshow('Homography', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

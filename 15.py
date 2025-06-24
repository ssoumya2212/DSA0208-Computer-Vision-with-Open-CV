import cv2
import numpy as np

img = cv2.imread('image.jpg')
rows, cols = img.shape[:2]

# Four point correspondences
pts_src = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
pts_dst = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])

# DLT using findHomography (method=0 forces DLT)
H, _ = cv2.findHomography(pts_src, pts_dst, method=0)
dlt_result = cv2.warpPerspective(img, H, (cols, rows))

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('DLT Result', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
cv2.imshow('DLT Result', dlt_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

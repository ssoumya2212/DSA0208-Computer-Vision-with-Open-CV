import cv2
import numpy as np

img = cv2.imread('image.jpg')
rows, cols = img.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [220, 220]])

M = cv2.getPerspectiveTransform(pts1, pts2)
perspective = cv2.warpPerspective(img, M, (cols, rows))

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Perspective Transformed', cv2.WINDOW_NORMAL)

cv2.imshow('Original', img)
cv2.imshow('Perspective Transformed', perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()

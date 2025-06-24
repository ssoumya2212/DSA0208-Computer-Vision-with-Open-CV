import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])
sharp = cv2.filter2D(img, -1, kernel)
cv2.imshow("Laplacian Diagonal Sharpen", sharp)
cv2.waitKey(0); cv2.destroyAllWindows()

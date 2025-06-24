import cv2
import numpy as np
def resize_and_show(title, img, width=600):
    h, w = img.shape[:2]
    scale = width / w
    resized = cv2.resize(img, (width, int(h * scale)))
    cv2.imshow(title, resized)

img = cv2.imread('image.jpg', 0)
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharp = cv2.filter2D(img, -1, kernel)
resize_and_show("Laplacian Positive Center", sharp)
cv2.waitKey(0); cv2.destroyAllWindows()

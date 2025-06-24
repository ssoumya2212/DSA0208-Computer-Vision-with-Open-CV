import cv2
import numpy as np
def resize_and_show(title, img, width=600):
    h, w = img.shape[:2]
    scale = width / w
    resized = cv2.resize(img, (width, int(h * scale)))
    cv2.imshow(title, resized)

img = cv2.imread('image.jpg', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
gradient = cv2.magnitude(sobelx, sobely)
gradient = np.uint8(gradient)
resize_and_show("Gradient Masking", gradient)
cv2.waitKey(0); cv2.destroyAllWindows()

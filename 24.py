import cv2
def resize_and_show(title, img, width=600):
    h, w = img.shape[:2]
    scale = width / w
    resized = cv2.resize(img, (width, int(h * scale)))
    cv2.imshow(title, resized)

img = cv2.imread('image.jpg', 0)
k = 1.5
blur = cv2.GaussianBlur(img, (9, 9), 10.0)
highboost = cv2.addWeighted(img, k, blur, -(k-1), 0)
resize_and_show("High-Boost", highboost)
cv2.waitKey(0); cv2.destroyAllWindows()

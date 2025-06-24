import cv2
def resize_and_show(title, img, width=600):
    h, w = img.shape[:2]
    scale = width / w
    resized = cv2.resize(img, (width, int(h * scale)))
    cv2.imshow(title, resized)

img = cv2.imread('image.jpg', 0)
blur = cv2.GaussianBlur(img, (9, 9), 10.0)
unsharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
resize_and_show("Unsharp Masking", unsharp)
cv2.waitKey(0); cv2.destroyAllWindows()

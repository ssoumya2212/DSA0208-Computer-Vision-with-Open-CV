import cv2
def resize_and_show(title, img, width=600):
    h, w = img.shape[:2]
    scale = width / w
    resized = cv2.resize(img, (width, int(h * scale)))
    cv2.imshow(title, resized)

image = cv2.imread('image.jpg')
roi = image[50:150, 50:150]
image[200:300, 200:300] = roi
resize_and_show("Cropped and Pasted", image)
cv2.waitKey(0); cv2.destroyAllWindows()

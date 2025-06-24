import cv2
def resize_and_show(title, img, width=600):
    h, w = img.shape[:2]
    scale = width / w
    resized = cv2.resize(img, (width, int(h * scale)))
    cv2.imshow(title, resized)

image = cv2.imread('image.jpg')
watermarked = image.copy()
cv2.putText(watermarked, 'Watermark', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (255, 255, 255), 2, cv2.LINE_AA)
resize_and_show("Watermarked", watermarked)
cv2.waitKey(0); cv2.destroyAllWindows()

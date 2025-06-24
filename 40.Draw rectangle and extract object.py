# Draw rectangle and extract object using OpenCV
import cv2

img = cv2.imread('input.jpg')
x, y, w, h = 100, 100, 200, 200  # Sample rectangle coords
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
roi = img[y:y+h, x:x+w]
cv2.imwrite('rectangle.jpg', img)
cv2.imwrite('extracted_object.jpg', roi)

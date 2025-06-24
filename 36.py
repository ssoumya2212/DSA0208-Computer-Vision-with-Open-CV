# Recognise watch from an image (simple object detection)
import cv2

img = cv2.imread('watch.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
watch_cascade = cv2.CascadeClassifier('watch_cascade.xml')  # Use custom cascade if available

watches = watch_cascade.detectMultiScale(gray, 1.1, 5)
for (x, y, w, h) in watches:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imwrite('detected_watch.jpg', img)

import cv2

img = cv2.imread('image.jpg')
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Clockwise: -90 degrees
clockwise = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_cw = cv2.warpAffine(img, clockwise, (w, h))

# Counterclockwise: +90 degrees
counterclockwise = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_ccw = cv2.warpAffine(img, counterclockwise, (w, h))

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Clockwise', cv2.WINDOW_NORMAL)
cv2.namedWindow('Counterclockwise', cv2.WINDOW_NORMAL)

cv2.imshow('Original', img)
cv2.imshow('Clockwise', rotated_cw)
cv2.imshow('Counterclockwise', rotated_ccw)
cv2.waitKey(0)
cv2.destroyAllWindows()

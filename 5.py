import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image was loaded
if img is None:
    print("Image not found. Check file path.")
    exit()

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(img, kernel, iterations=1)

# Show images in actual size (no resizing if image is small)
cv2.imshow('Original Image', img)
cv2.imshow('Eroded Image', eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

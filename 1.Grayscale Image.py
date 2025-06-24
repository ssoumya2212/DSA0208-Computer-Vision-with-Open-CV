import cv2

# Read the image
img = cv2.imread('image.jpg')

# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize the grayscale image to fit screen (e.g., width = 600)
resized = cv2.resize(gray, (600, int(gray.shape[0] * 600 / gray.shape[1])))

# Display resized image
cv2.imshow('Grayscale Image (Resized)', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Read the image
img = cv2.imread('image.jpg')

# Check if image is loaded
if img is None:
    print("Image not found.")
    exit()

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (7, 7), 0)

# Resize the blurred image to fit screen (e.g., width = 600)
resized_blur = cv2.resize(blur, (600, int(blur.shape[0] * 600 / blur.shape[1])))

# Display the resized blurred image
cv2.imshow('Blurred Image (Resized)', resized_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

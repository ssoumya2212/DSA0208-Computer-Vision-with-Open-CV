import cv2

# Read image in color mode
img = cv2.imread('image.jpg')

# Check if image is loaded
if img is None:
    print("Image not found. Check file name/path.")
    exit()

# Get original dimensions
height, width = img.shape[:2]

# Resize for smaller and bigger versions
smaller = cv2.resize(img, (width // 2, height // 2))
bigger = cv2.resize(img, (int(width * 1.5), int(height * 1.5)))

# Create resizable windows (no zooming)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Smaller Size', cv2.WINDOW_NORMAL)
cv2.namedWindow('Bigger Size', cv2.WINDOW_NORMAL)

# Show images without forced resizing
cv2.imshow('Original', img)
cv2.imshow('Smaller Size', smaller)
cv2.imshow('Bigger Size', bigger)

cv2.waitKey(0)
cv2.destroyAllWindows()

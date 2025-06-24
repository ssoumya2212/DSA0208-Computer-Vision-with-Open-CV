import cv2

cap = cv2.VideoCapture(0)
print("Press 's' = slow, 'f' = fast, 'q' = quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    resized = cv2.resize(frame, (640, 480))  # Resize for consistent display
    cv2.imshow('Webcam', resized)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.waitKey(60)  # Slow
    elif key == ord('f'):
        cv2.waitKey(10)  # Fast
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

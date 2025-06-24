import cv2

cap = cv2.VideoCapture('video.mp4')  # or '0' for webcam

# Slow Motion
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    resized = cv2.resize(frame, (640, 480))  # Avoid zooming
    cv2.imshow('Slow Motion', resized)
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset

# Fast Motion
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    resized = cv2.resize(frame, (640, 480))
    cv2.imshow('Fast Motion', resized)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

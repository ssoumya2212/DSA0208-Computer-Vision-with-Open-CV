import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rows, cols = frame.shape[:2]
    pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
    pts2 = np.float32([[10, 100], [cols - 10, 50], [50, rows - 100], [cols - 50, rows - 50]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    transformed = cv2.warpPerspective(frame, M, (cols, rows))

    cv2.imshow('Original Video', frame)
    cv2.imshow('Perspective Video', transformed)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

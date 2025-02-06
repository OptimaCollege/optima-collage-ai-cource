import cv2
import face_recognition

img = cv2.imread('image.jpg')

# Detect faces
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
face_locations = face_recognition.face_locations(img)

for y1, x1, y2, x2, in face_locations:
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)
cv2.waitKey(0)


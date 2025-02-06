import cv2
import dlib

img = cv2.imread('image.jpg')
h = img.shape[0]
w = img.shape[1]

# Create detector
detector = dlib.get_frontal_face_detector()

# Detect faces
wimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faceRects = detector(wimg, 0)

bboxes = []
for faceRect in faceRects:
    cvRect = [
        int(faceRect.left()), int(faceRect.top()),
        int(faceRect.right()), int(faceRect.bottom())
        ]

    bboxes.append(cvRect)
    cv2.rectangle(img, (cvRect[0], cvRect[1]), (cvRect[2], cvRect[3]),  (0, 255, 0),
                  int(round(h / 150)), 4)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)

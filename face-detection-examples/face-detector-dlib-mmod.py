import cv2
import dlib

img = cv2.imread('image.jpg')
h = img.shape[0]
w = img.shape[1]

# Create detector
detector = dlib.cnn_face_detection_model_v1('data/mmod_human_face_detector.dat')

# Detect faces
wimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faceRects = detector(wimg, 0)
print(faceRects)
bboxes = []
for faceRect in faceRects:
    cvRect = [
        int(faceRect.rect.left()), int(faceRect.rect.top()),
        int(faceRect.rect.right()), int(faceRect.rect.bottom())
        ]

    bboxes.append(cvRect)
    cv2.rectangle(img, (cvRect[0], cvRect[1]), (cvRect[2], cvRect[3]),  (0, 255, 0),
                  int(round(h / 150)), 4)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)

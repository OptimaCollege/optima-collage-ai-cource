import cv2

img = cv2.imread('image.jpg')
h = img.shape[0]
w = img.shape[1]

# Load DNN model
modelFile = "data/res10_300x300_ssd_iter_140000_fp16.caffemodel"
configFile = "data/deploy.prototxt.txt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

# Prepare image
blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), [104, 117, 123],
                             False, False)

# Detect faces
net.setInput(blob)
detections = net.forward()

bboxes = []
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.8:
        x1 = int(detections[0, 0, i, 3] * w)
        y1 = int(detections[0, 0, i, 4] * h)
        x2 = int(detections[0, 0, i, 5] * w)
        y2 = int(detections[0, 0, i, 6] * h)
        bboxes.append([x1, y1, x2, y2])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), int(round(h / 150)), 8)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)


import cv2 as cv

img = cv.imread('group.jpg')
#cv.imshow('Person', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2)
print(f'Number of faces = {len(faces_rect)}')
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv.imshow('Detected faces', img)
cv.waitKey(0)

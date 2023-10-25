
import cv2
import numpy as np
import time

pic=cv2.imread('image.jpg')

col=int(pic.shape[0]//4)
row=int(pic.shape[1]//4)


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray=cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05, minNeighbors=5)

print(faces)

for x,y,w,h in faces:
	img=cv2.rectangle(pic,(x,y),(x+w,y+h), (0,255,0), 3)

img = cv2.resize(img,(row,col))

cv2.imshow('picture.jpg',img)

print(len(faces))

cv2.waitKey(0)

cv2.destroyAllWindows()

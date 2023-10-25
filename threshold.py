import cv2
import numpy

pic= cv2.imread("picture.jpg",0)

threshold=100

(T_VALUE,binary_threshold)= cv2.threshold(pic,threshold,255,cv2.THRESH_BINARY_INV)

cv2.imshow('Deepak',binary_threshold)

cv2.waitKey()

cv2.destroyAllWindows()


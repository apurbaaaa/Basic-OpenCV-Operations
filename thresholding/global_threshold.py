import os 
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bear.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
#noise removal
thresh = cv2.blur(thresh, (10, 10))
ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY) #80 is th threshold value, all values above 80 = 255 below 80 = 0


cv2.imshow('Bear', img)
cv2.imshow('Threshold impl', thresh)
cv2.waitKey(0)

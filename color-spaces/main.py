import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'deer.jpeg'))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #position of blue and red changed
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite(os.path.join('.', 'data', 'RGBdeer.jpeg'), img_rgb)
cv2.imwrite(os.path.join('.', 'data', 'GRAYdeer.jpeg'), img_gray)
cv2.imwrite(os.path.join('.', 'data', 'HSVdeer.jpeg'), img_hsv)

cv2.imshow('Image', img)
cv2.imshow('Converted Image', img_rgb)
cv2.imshow('GRAY', img_gray)
cv2.imshow('HSV', img_hsv)
cv2.waitKey(0)
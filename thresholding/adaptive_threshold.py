import os 
import cv2
#for lighting difference

img = cv2.imread(os.path.join('.', 'data', 'handwritten.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('Adaptive Threshold', thresh)
cv2.waitKey()
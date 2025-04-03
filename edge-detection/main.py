import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'deer.jpeg'))

img_canny = cv2.Canny(img, 150, 500)

img_dilate = cv2.dilate(img_canny, np.ones((5, 5), dtype=np.int8))

img_erode = cv2.erode(img_dilate, np.ones((5, 5), dtype=np.int8))
cv2.imshow('Canny Impl', img_erode)
cv2.waitKey(0)
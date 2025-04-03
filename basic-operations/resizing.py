import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'dog.jpeg'))
print(img.shape)
output_path = os.path.join('.', 'data', 'dog_resized.jpeg')
resized_img = cv2.resize(img, (640, 480))#(height, width), shape print garda ulto aaucha
print(resized_img.shape)

cv2.imwrite(output_path, resized_img)
cv2.imshow('Image of a dog', img)
cv2.imshow('Image of resized dog', resized_img)
cv2.waitKey(0)
import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'dog.jpeg'))
print(img.shape)
output_path = os.path.join('.', 'data', 'dog_cropped.jpeg')
cropped_img = img[1296:2592, 1728:3456]#intervals selected for crop of the numpy img array

cv2.imwrite(output_path, cropped_img)
cv2.imshow('img', cropped_img)
cv2.waitKey(0)
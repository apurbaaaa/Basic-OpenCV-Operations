import os
import cv2
#blur is used for noise removal
img = cv2.imread(os.path.join('.', 'data', 'noise.jpg'))
output_path = os.path.join('.', 'data', 'blurrednoise.jpeg')
output_path_gau = os.path.join('.', 'data', 'blurrednoisegau.jpeg')
output_path_med = os.path.join('.', 'data', 'blurrednoisemed.jpeg')
k_size = 7
img_blur = cv2.blur(img,(k_size, k_size))
img_gau_blur = cv2.GaussianBlur(img, (k_size, k_size), 6)
img_med_blur = cv2.medianBlur(img, k_size)
cv2.imwrite(output_path, img_blur)
cv2.imwrite(output_path_gau, img_gau_blur)
cv2.imwrite(output_path_med, img_med_blur)
cv2.imshow('Image', img)
cv2.imshow('Image Blurred', img_blur)
cv2.imshow('Image Blurred Gaussian', img_gau_blur)
cv2.imshow('Image Blurred Median', img_med_blur)


cv2.waitKey(0)
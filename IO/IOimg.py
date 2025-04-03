import cv2
import os

#reading an image
image = cv2.imread('./data/deer.jpeg')
print(image.shape) #a numpy array

#writing an image
output_path = os.path.join('.', 'data', 'deer_out.jpeg')
cv2.imwrite(output_path, image)
print(f"Image saved at: {os.path.abspath(output_path)}")

#visualizing an image
cv2.imshow('image', image)
cv2.waitKey(0) #visualize  until 0 is pressed, if forgotten openCV opens the image and immediately closes it 
#param tells how many ms the window is to be open, except 0, 0 means manual closing



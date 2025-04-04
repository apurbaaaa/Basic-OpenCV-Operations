import os 
import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))

#line
print(img.shape)
cv2.line(img, (100, 150), (250, 300), (0, 255, 0), 3)#x coodinates, y coordinates, color, thickness

#rectangle 
cv2.rectangle(img, (100, 100), (400, 300), (255, 0, 0), 5)

#circle
cv2.circle(img, (50, 50), 15, (0, 0, 255), -1) #img, center, radius, color, thickness, -1 is opaque

#text
cv2.putText(img, 'Hello, World!', (30, 300), cv2.FONT_HERSHEY_SIMPLEX, 2,  (255, 0, 255), 2)#img, text, starting point, font, size , color, color

cv2.imshow("Whiteboard", img)
cv2.waitKey(0)
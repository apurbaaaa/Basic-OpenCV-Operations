import cv2
import os

#read video
video_path = os.path.join('.', 'data', 'flowers.mp4')
video = cv2.VideoCapture(video_path)
# print(video.shape) does not run

#visualize video
ret = True
while ret:
    ret, frame = video.read() #read frames, ret = false when no frames are left
    if ret: #only if ret is present
        cv2.imshow('frame', frame)
        cv2.waitKey(34)#because vid is of 30fps and 1/30 = 0.03333s which is 33.33 ms

video.release()
cv2.destroyAllWindows()
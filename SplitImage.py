# Importing all necessary libraries
import cv2
import os
# Read the video from specified path
cam = cv2.VideoCapture("E:\\MDCS\\LAB\\EXP6\\vid.mp4")
try:
# creating a folder named data
if not os.path.exists('data'):
os.makedirs('data')
# if not created then raise error
except OSError:
print ('Error: Creating directory of data')
# frame
currentframe = 0
while(True):
# reading from frame
ret,frame = cam.read()
if ret:
# if video is still left continue creating images
name = './data/frame' + str(currentframe) + '.jpg' print ('Creating...' + name)
# writing the extracted images
cv2.imwrite(name, frame)
Ex.No:06 Write a program to split images froma video without usingany primitives. Date:
# increasing counter so that it will
# show how many frames are created
currentframe += 1
else:
break
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
Run the command:
>python filename.py
Then a new directory will be created which will contain all the images. Thus the video is converted/split into images. 
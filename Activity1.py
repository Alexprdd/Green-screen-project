import cv2
import numpy
import time

store_video=cv2.VideoCapture("video.mp4")
print(store_video.read())

for i in range(60):
    return_value,bg=store_video.read()
    if return_value==False:
        continue
count=0
time.sleep(1)
while (store_video.isOpened()):
    return_value,img=store_video.read()
    if not return_value:
        break
    count+=1
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red=numpy.array([100,40,40])
    upper_red=numpy.array([100,255,255])
    mask1=cv2.inRange(hsv, lower_red,upper_red)
    lower_red=numpy.array([150,40,40])
    upper_red=numpy.array([180,255,255])
    mask2=cv2.inRange(hsv, lower_red,upper_red)
    mask1=mask1+mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN, numpy.ones((3,3),numpy.uint8),iterations=2)
    mask1=cv2.dilate(mask1,numpy.ones((3,3),numpy.uint8),iterations=1)
    mask2=cv2.bitwise_not(mask1)
    res1=cv2.bitwise_and(bg,bg,mask=mask1)
    res2=cv2.bitwise_and(img,img,mask=mask2)
    final=cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("0",res2) #res1,res2,final
    k=cv2.waitKey(10)
    if k==27:
        break
    




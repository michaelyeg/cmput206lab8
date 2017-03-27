import cv2
import numpy as np

img = cv2.imread('coins.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

# Copied and modified from http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html#theory
circles = cv2.HoughCircles(img, method=cv2.HOUGH_GRADIENT, dp=1, minDist=70,
                            param1=50,param2=30,minRadius=30, maxRadius=90)
# minDist, minRadius and max Radius are modified to suit the specific input picture.

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
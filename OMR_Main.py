import cv2
import numpy as np

##########################
path = "1.jpg"
widthImg = 700
heightImg = 700
#########################
img = cv2.imread(path)

img = cv2.resize(img,(widthImg,heightImg))
#imgGray = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
#imgCanny =cv2.Canny(imgBlur,10,50)



cv2.imshow("Original", img)
cv2.waitKey(0)
import cv2
import numpy as np
import utlis

##########################
path = "1.jpg"
widthImg = 700
heightImg = 700
#########################
img = cv2.imread(path)

img = cv2.resize(img, (widthImg, heightImg))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
imgCanny = cv2.Canny(imgBlur, 10, 50)

imageArray = ([img, imgGray,imgBlur,imgCanny])
imgStacked = utlis.stackImages(imageArray, 0.5)

cv2.imshow("Stacked Images", imgStacked)
cv2.waitKey(0)

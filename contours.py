import cv2 as cv
import numpy as np

PATH = r"C:\Users\rames\Downloads\img_vid\img\IOT.jpg"

img = cv.imread(PATH)
img = cv.resize(img, (500,500))

#convert to grey scale
grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("grey", grey)

#edge detection
canny = cv.Canny(img, 150, 255)
cv.imshow("canny", canny)

#thresolding
ret, thresh = cv.threshold(grey, 127, 255, cv.THRESH_BINARY)
cv.imshow("tresh", thresh)

#contours
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)}")

#draw contours on blank image
blank = np.zeros(img.shape[:3], dtype= 'uint8')
print(f"Shape of blank image: {blank.shape}")

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contour', blank)

#draw contours in image
cv.drawContours(img, contours, -1, (0, 255, 0), 1)
cv.imshow('Contours', img)



cv.waitKey(0)
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = r"C:\Users\rames\Downloads\img_vid\img\IOT.jpg"

img = cv.imread(PATH)
img = cv.resize(img, (500,500))
cv.imshow("real", img)

#blur
blur = cv.blur(img,(5,5))
cv.imshow("blur", blur)

#bilateral
bilater = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilater)

#midian
median = cv.medianBlur(img, 3)
cv.imshow("median", median)

cv.waitKey(0)
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = r"C:\Users\rames\Downloads\img_vid\img\IOT.jpg"

img = cv.imread(PATH)
img = cv.resize(img, (500,500))

blank = np.zeros((500,500), dtype='uint8')


mask = cv.circle(blank.copy(),(200,200), 100, 255,-1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("masked", masked)

cv.waitKey(0)
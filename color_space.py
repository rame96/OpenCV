import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = r"C:\Users\rames\Downloads\img_vid\img\IOT.jpg"

img = cv.imread(PATH)
img = cv.resize(img, (500,500))

#convert to grey scale
grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("grey", grey)

#hsv
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
cv.imshow("hsv", hsv)

#LAB
lab = cv.cvtColor(img, cv.COLOR_RGB2LAB)
cv.imshow("lab", lab)

plt.imshow(img)
plt.show()

cv.waitKey(0)
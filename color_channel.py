import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = r"C:\Users\rames\Downloads\img_vid\img\IOT.jpg"

img = cv.imread(PATH)
img = cv.resize(img, (500,500))

#split
g,b,r = cv.split(img)
cv.imshow("green",g)
cv.imshow("blue",b)
cv.imshow("red",r)

#merged
merged = cv.merge([g,b,r])
cv.imshow("merged", merged)
cv.waitKey(0)
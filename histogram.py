import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = r"C:\Users\rames\Downloads\img_vid\img\IOT.jpg"

img = cv.imread(PATH)
img = cv.resize(img, (500,500))

#plotting grey scale image
grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("grey", grey)

hist = cv.calcHist([grey], [0], None,[256], [0,255])

plt.figure()
plt.title("HIST")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(hist)
plt.show()

#for plotting RGB
plt.figure()
plt.title("HIST_RGB")
plt.xlabel("X")
plt.ylabel("Y")

cols = ("b", "g", "r")
for i, col in enumerate(cols):
    hist = cv.calcHist([img], [i], None,[256], [0,255])
    plt.plot(hist, color = col)

plt.show()
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((400,400), dtype='uint8')

rect = cv.rectangle(img.copy(), (50,50), (300,300),255,-1)
cv.imshow("rectangle", rect)

cir = cv.circle(img.copy(),(200,200), 150, 255,-1)
cv.imshow("circle", cir)

#bitwise and operation

#only intercepting point
bit_and = cv.bitwise_and(rect,cir)
cv.imshow("AND",bit_and)

#all points
bit_or = cv.bitwise_or(rect,cir)
cv.imshow("or",bit_or)

#opposite of AND
bit_xor = cv.bitwise_xor(rect,cir)
cv.imshow("xor",bit_xor)

#inverse
bit_not = cv.bitwise_not(cir)
cv.imshow("not",bit_not)

cv.waitKey(0)
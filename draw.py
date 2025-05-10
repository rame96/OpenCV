import cv2 as cv
import numpy as np

PATH = r"C:\Users\rames\Downloads\img_vid\img\CAR.jpg"
VIDIO_PATH = r"C:\Users\rames\Downloads\vid.mp4"

# creating blank image
blank = np.zeros((500,500,3), dtype = 'uint8')
blank[:] = 0,255,0
cv.imshow("Green", blank)

#painting the image

blank[200:300,300:500] = 0,0,255
cv.imshow("red", blank)

#draw rectangle

cv.rectangle(blank, (0,0), (250,250), (0,0,255), 2)
cv.imshow("rectangle", blank)

# #fill the rectangle
cv.rectangle(blank, (50,50), (250,500), (0,0,255), cv.FILLED) #or use -1 to fill
cv.imshow("rectangle", blank)

# #draw the circle
cv.circle(blank, (250,250), 50, (0,250,0), -1)
cv.imshow("cicle", blank)

#draw line

cv.line(blank, (0,0), (250,250), (255,0,0), 1)
cv.imshow("line", blank)

#write text

cv.putText(blank, "Face", (255,255), cv.FONT_HERSHEY_PLAIN, 2.0, (255,255,255),2)
cv.imshow("with_text", blank)

cv.waitKey(0)
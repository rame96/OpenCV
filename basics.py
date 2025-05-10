import cv2 as cv

PATH = r"C:\Users\rames\Downloads\th (16).jpeg"

# #RGB 2 GREY
img = cv.imread(PATH)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("car",grey)

#BLUR AN IMAGE
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur",blur)


#edge cascade

edge = cv.Canny(blur, 125, 175)
cv.imshow("edge", edge)

#dilating the image

dilated = cv.dilate(edge,(3,3), iterations=1)
cv.imshow("dilated", dilated)


#eroding(reverse dilating)

eroding = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("erode", eroding)

#resize

resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("resize", resize)

#crop
cv.imshow("crop",resize[100:500,100:400])
cv.waitKey(0)
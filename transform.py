import cv2 as cv
import numpy as np

PATH = r"C:\Users\rames\Downloads\th (16).jpeg"

img = cv.imread(PATH)

#translation

def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimention = (image.shape[1],image.shape[0])
    return cv.warpAffine(image, transMat, dimention)

#-x --> left
#-y --> up
#x --> right
#y --> down

def rotation(image, angle, rot_point = None):
    (width, height) = image.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height/2)
    
    rotMat = cv.getRotationMatrix2D(rot_point,angle,scale =1.0)
    dimention = (width, height)
    return cv.warpAffine(image, rotMat, dimention)

#transpose
trans = translate(img, 50, 50)
cv.imshow("transpose", trans)

#rotating
rot = rotation(img, 45)
cv.imshow("rotate", rot)

#flipping

flip = cv.flip(img,1)
cv.imshow("flip", flip)

cv.waitKey(0)
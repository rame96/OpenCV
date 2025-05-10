import cv2 as cv


PATH = r"C:\Users\rames\Downloads\img_vid\img\too_big.jpg"
VIDIO_PATH = r"C:\Users\rames\Downloads\vid.mp4"

#reading images
img = cv.imread(PATH)
cv.imshow("Image", img)

def change_res(width, height):
    #live videos
    capture.set(3, width)
    capture.set(4,height)

#resizing image, videos etc
def reshape(image, scale):
    height = int(image.shape[0]*scale)
    weidth = int(image.shape[1]*scale)
    return (height, weidth)

scaled_img = cv.resize(img,reshape(img, 0.5),interpolation=cv.INTER_AREA)

cv.imshow("Scaled_Image", scaled_img)

cv.waitKey(2000)
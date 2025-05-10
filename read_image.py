import cv2 as cv

PATH = r"C:\Users\rames\Downloads\img_vid\img\CAR.jpg"
VIDIO_PATH = r"C:\Users\rames\Downloads\vid.mp4"

#reading images
img = cv.imread(PATH)
cv.imshow("Image", img)

#reading videos

capture = cv.VideoCapture(VIDIO_PATH)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
 
capture.release()
cv.destroyAllWindows()


cv.waitKey(0)
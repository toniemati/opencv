import cv2
import imutils

image = cv2.imread('image.jpeg')

i = 15

while i <= 360:
    rotated = imutils.rotate(image, i)
    cv2.imshow('Rotated', rotated)
    i += 15
    cv2.waitKey(500)

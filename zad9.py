import cv2
import imutils

image = cv2.imread('image.jpeg')

rotated = imutils.rotate(image, 75)

cv2.imshow('', rotated)

cv2.imwrite('image_rotated.jpeg', rotated)


import cv2
import imutils

image = cv2.imread('image.webp')

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=w//5, inter=cv2.INTER_AREA)
resized2 = imutils.resize(image, width=w//5, inter=cv2.INTER_LINEAR)

cv2.imshow('Resized AREA', resized)
cv2.imshow('Resized2 LINEAR', resized2)

cv2.waitKey(0)
cv2.destroyAllWindows()

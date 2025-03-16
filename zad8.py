import cv2
import imutils

image = cv2.imread('image.webp')

(h, w) = image.shape[:2]

resized1 = imutils.resize(image, width=w*4, inter=cv2.INTER_CUBIC)
resized2 = imutils.resize(image, width=w*4, inter=cv2.INTER_LANCZOS4)

cv2.imshow('Resized CUBIC', resized1)
cv2.imshow('Resized2 LANCZNOS4', resized2)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import imutils

image = cv2.imread('image.jpeg')

rotated = imutils.rotate(image, 180)

cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

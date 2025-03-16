import cv2
import imutils

image = cv2.imread('image.jpeg')

rotated = imutils.rotate(image, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)

# rotated = imutils.rotate(image, 90)

cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

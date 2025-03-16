import cv2
import imutils

image = cv2.imread('image.jpg')

cv2.imshow('Original', image)

shifted = imutils.translate(image, 100, 50)

cv2.imshow("Shifted", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
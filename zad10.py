import cv2
import imutils

image = cv2.imread('image.webp')

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=800)

cv2.imwrite('image_resized.webp', resized)

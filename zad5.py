import cv2
import numpy as np

image = cv2.imread('image.jpg')
image_translated = cv2.imread('image_translated.jpeg')

diff = cv2.absdiff(image, image_translated)

cv2.imshow('diff', diff)
cv2.waitKey(0)
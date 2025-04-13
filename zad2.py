import cv2
import numpy as np

image = cv2.imread('image.jpg')

M = np.ones(image.shape, dtype="uint8") * 150

added = cv2.add(image, M)

cv2.imshow('Lighter', added)
cv2.waitKey(0)
cv2.destroyAllWindows()

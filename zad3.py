import cv2
import numpy as np

image = cv2.imread('image.jpg')

M = np.ones(image.shape, dtype="uint8") * 80

subtracted = cv2.subtract(image, M)
# subtracted = np.uint8(image) - np.uint8(M)

cv2.imshow('Darker', subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()

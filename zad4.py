import cv2
import numpy as np

image = cv2.imread('image.jpg')

B, G, R = cv2.split(image)

R = cv2.add(R, 30)
G = cv2.subtract(G, 20)
B = cv2.add(B, 10)

ig = cv2.merge([B, G, R])

cv2.imshow('ig', ig)
cv2.waitKey(0)
cv2.destroyAllWindows()

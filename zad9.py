import cv2
import imutils
from math import floor

image = cv2.imread('image.webp')

(h, w) = image.shape[:2]

i = 100

while i <= 300:
    resized = imutils.resize(image, width=floor(w*(i/100)))
    cv2.imshow(f"Resized by: {i}%", resized)
    i += 20
    cv2.waitKey(500)

cv2.destroyAllWindows()

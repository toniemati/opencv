import cv2
import imutils

image = cv2.imread('image.jpeg')

rotated1 = imutils.rotate(image, 60)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated2 = cv2.warpAffine(image, M, (w, h))

cv2.imshow('Rotated 1', rotated1)
cv2.imshow('Rotated 2', rotated2)

cv2.waitKey(0)
cv2.destroyAllWindows()

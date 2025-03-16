import cv2

image = cv2.imread('image.jpeg')

(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((0,0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
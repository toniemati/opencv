import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

right_image = image[:, w//2:]

cv2.imshow('right', right_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

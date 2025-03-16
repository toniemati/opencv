import cv2

image = cv2.imread('image.webp')

(h, w) = image.shape[:2]

cv2.imshow('Original', image)

resized = cv2.resize(image, (w*2, h*2), interpolation=cv2.INTER_LINEAR)

cv2.imshow('Resized', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

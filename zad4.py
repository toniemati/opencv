import cv2

image = cv2.imread('image.webp')

cv2.imshow('Original', image)

(h, w) = image.shape[:2]

resized1 = cv2.resize(image, (h*3, w*3), interpolation=cv2.INTER_NEAREST)
resized2 = cv2.resize(image, (h*3, w*3), interpolation=cv2.INTER_LINEAR)
resized3 = cv2.resize(image, (h*3, w*3), interpolation=cv2.INTER_CUBIC)
resized4 = cv2.resize(image, (h*3, w*3), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('Resized INTER_NEAREST', resized1)
cv2.imshow('Resized INTER_LINEAR', resized2)
cv2.imshow('Resized INTER_CUBIC', resized3)
cv2.imshow('Resized INTER_LANCZOS4', resized4)

cv2.waitKey(0)
cv2.destroyAllWindows()

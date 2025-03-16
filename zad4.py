import cv2

image = cv2.imread('image.webp')

flipped1 = cv2.flip(image, -1)
flipped2 = cv2.flip(image, 0)
flipped3 = cv2.flip(image, 1)

cv2.imshow("Original", image)
cv2.imshow("Flipped 1", flipped1)
cv2.imshow("Flipped 2", flipped2)
cv2.imshow("Flipped 3", flipped3)

cv2.waitKey(0)
cv2.destroyAllWindows()

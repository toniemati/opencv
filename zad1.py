import cv2

image = cv2.imread('image.webp')

flipped = cv2.flip(image, 1)

cv2.imshow("Flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()

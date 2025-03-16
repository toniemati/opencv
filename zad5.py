import cv2

image = cv2.imread('image.webp')

(h, w) = image.shape[:2]

flipped = cv2.flip(image[0:500,0:500], -1)

image[0:500,0:500] = flipped

cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

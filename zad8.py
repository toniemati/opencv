import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

image[0:100, 0:w-1] = (0, 0, 255)

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

image = cv2.imread('image.jpg')

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w) = image.shape[:2]
(b, g, r) = image[0, 0]
image[h-10:h-1, w-10:w-1] = (0, 0, 255)

cv2.imshow("Red corner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

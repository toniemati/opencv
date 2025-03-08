import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

image[0:h//2, 0:w//2] = (0, 255, 0)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
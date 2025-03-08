import cv2

image = cv2.imread("image.jpg")

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)
cv2.resizeWindow("Image", 200, 200)
cv2.waitKey(0)
cv2.destroyAllWindows()
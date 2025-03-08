import cv2

# img1 = cv2.imread("example.jpg") # wrong file name
image = cv2.imread("image.jpg")

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
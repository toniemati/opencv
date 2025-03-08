import cv2

# img1 = cv2.imread("example.jpg") # wrong file name
img1 = cv2.imread("image.jpg")
img2 = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

print(cv2.WINDOW_NORMAL)

cv2.namedWindow("Image 1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Image 2", cv2.WINDOW_NORMAL)
cv2.namedWindow("Image 3", cv2.WINDOW_NORMAL)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Image 3", img1)

cv2.resizeWindow("Image 3", 200, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w, c) = img1.shape[:3]
(h, w) = img2.shape[:2]  # no channels in grayscale
print(f"color img channels: {c}")

cv2.imwrite("image_gray.jpg", img2)

import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

x = w // 3
y = h // 3

cropped = image[y:y*2, x:x*2]

cv2.imshow("Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

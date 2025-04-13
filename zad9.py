import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

cropped = image[0:300, 300:600]

cv2.imwrite('cropped.jpg', cropped)

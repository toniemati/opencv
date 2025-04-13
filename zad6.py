import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

cropped = image[0:100, 0:100]

image[h//2:h//2+100, w//2:w//2+100] = image[0:100, 0:100]

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

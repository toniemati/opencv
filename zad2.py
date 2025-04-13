import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

bot_image = image[h//2:]

cv2.imshow('bottom', bot_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

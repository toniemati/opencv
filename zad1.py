import cv2

image = cv2.imread('image.jpg')

cropped_image = image[0:500, 0:500]

cv2.imshow('cropped', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
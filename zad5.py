import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

start_x = 510
end_x = 710
start_y = 790
end_y = 990

cropped = image[start_x:end_x, start_y:end_y]

cv2.imshow('cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

start_x = int(input('Podaj start x: '))
end_x = int(input('Podaj end x: '))
start_y = int(input('Podaj start y: '))
end_y = int(input('Podaj end y: '))


cropped = image[start_x:end_x, start_y:end_y]

cv2.imshow('cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import imutils

tx = input('Podaj przesuniecie w poziomie: ')
ty = input('Podaj przesuniecie w pionie: ')

print(tx,ty)

image = cv2.imread('image.jpg')

cv2.imshow('Original', image)

shifted = imutils.translate(image, tx, ty)

cv2.imshow("Shifted", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
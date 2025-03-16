import cv2

image = cv2.imread('image.webp')

r = int(input('Podaj sposób odbicia: (0 – pionowe, 1 – poziome, -1 – oba): '))

flipped = cv2.flip(image, r)

cv2.imshow('Rotated', flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()

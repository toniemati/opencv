import cv2


image = cv2.imread('image.jpeg')


(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

r = int(input('Podaj kat obrotu: '))

M = cv2.getRotationMatrix2D((cX, cY), r, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

offset_x = 100

from_x = 0
to_x = offset_x
from_y = h//2
to_y = h//2+100


while to_x + offset_x < w:
    img = image.copy()
    
    img[from_y:to_y, from_x:to_x] = image[from_y:to_y, 0:100]
    
    cv2.imshow('image', img)
    cv2.waitKey(500)
    from_x += offset_x
    to_x += offset_x

cv2.waitKey(0)

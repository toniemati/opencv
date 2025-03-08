import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

x = int(input('x: '))
y= int(input('y: '))

if x >= 0 and x < w and y >= 0 and y < h:
    image[y - 5:y + 5, x - 5:x + 5] = (0, 0, 255)
    

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

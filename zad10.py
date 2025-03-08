import cv2

image = cv2.imread('image.jpg')

(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[200, 200]

print(f"r: {r1-r2}, g: {g1-g2}, b: {b1-b2}")
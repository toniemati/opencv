import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
(b, g, r) = image[cY, cX]

print(f"Center: {cX}:{cY}")
print(f"Pixel at center - Red: {r}, Green: {g}, Blue: {b}")
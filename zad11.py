import cv2

image = cv2.imread('image.jpg')

[h, w] = image.shape[:2]

max, red, green, blue = 0, 0, 0, 0
xx, yy = 0, 0

for y in range(0, h - 1):
    for x in range(0, w - 1):
        (b, g, r) = image[y, x]
        s = int(r)+int(b)+int(g)

        if s > max:
            max, red, green, blue, xx, yy = s, r, g, b, x, y
print(f"Pixel with the highest sum of colors: Red: {red}, Green: {green}, Blue: {blue}")
print(f"Sum of colors: {max}")
print(f"Coordinates: {xx}:{yy}")

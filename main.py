import cv2

image = cv2.imread('image.jpg')

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w) = image.shape[:2]
(b, g, r) = image[0, 0]
image[h-10:h-1, w-10:w-1] = (0, 0, 255)

cv2.imshow("Red corner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Height: {h}, Width: {w}")
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")

(cX, cY) = (w // 2, h // 2)

print(f"Center: {cX}:{cY}")
(b, g, r) = image[cY, cX]
print(f"Pixel at center - Red: {r}, Green: {g}, Blue: {b}")

# input_x = int(input('x: '))
# input_y = int(input('y: '))

# if input_x >= 0 and input_x < w and input_y >= 0 and input_y < h:
#     (b, g, r) = image[input_y, input_x]

#     print(f"Pixel at ({input_x}, {input_y}) - Red: {r}, Green: {g}, Blue: {b}")

#     image[input_y - 5:input_y + 5, input_x - 5:input_x + 5] = (0, 0, 255)

#     cv2.imshow("Red input", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Invalid coordinates")

image[0:cY, 0:cX] = (0, 255, 0)

cv2.imshow("Green rect", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image[cY-50:cY+50, cX-50:cX+50] = (0, 0, 255)

cv2.imshow("Red center", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(x3, y3) = (w // 3, h // 3)

center_img = image[y3:y3*2, x3:x3*2]

cv2.imshow("Center", center_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

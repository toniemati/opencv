import cv2

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]

width = w//3
height = h//3

for i in range(3):
    for j in range(3):
        from_x = i * height
        to_x = i * height + height
        from_y = j * width
        to_y = j * width + width

        img = image[from_x:to_x-1, from_y:to_y-1]
        cv2.imshow('img', img)
        cv2.waitKey(1000)

cv2.destroyAllWindows()

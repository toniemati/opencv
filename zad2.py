import cv2

# img1 = cv2.imread("example.jpg") # wrong file name
image = cv2.imread("image.jpg")

(h, w, c) = image.shape[:3]

print(f"Channels: {c}")

import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

print(img.shape)

x, y, w, h = 200, 30, 500, 450
cropped_img = img[y:y+h, x:x+w]
print(cropped_img.shape)

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)

# Координати прямокутника (ROI – region of interest):
# x – початок по горизонталі (зсув від лівого краю);
# y – початок по вертикалі (зсув від верхнього краю);
# w (width) – ширина вирізаного фрагмента;
# h (height) – висота вирізаного фрагмента.
# Тобто вирізана область визначається як image[y : y+h, x : x+w].

# У OpenCV (Python) координати починаються з верхнього лівого кута (0,0).

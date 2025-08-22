import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))
print(img.shape)

resized_img = cv2.resize(img, (640, 480))
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(2000)

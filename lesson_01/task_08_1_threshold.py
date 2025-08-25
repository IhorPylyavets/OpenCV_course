import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh_blur = cv2.blur(thresh, (10, 10))
ret, thresh = cv2.threshold(thresh_blur, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

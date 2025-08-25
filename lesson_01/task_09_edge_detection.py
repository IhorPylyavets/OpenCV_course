import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'basketball_player.png'))

edge_img = cv2.Canny(img, 100, 200)
#edge_img_50 = cv2.Canny(img, 50, 200)
#edge_img_20 = cv2.Canny(img, 50, 300)
edge_img_d = cv2.dilate(edge_img, np.ones((3, 3), dtype=np.int8))
edge_img_e = cv2.erode(edge_img_d, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('edge_img', edge_img)
#cv2.imshow('edge_img_50', edge_img_50)
#cv2.imshow('edge_img_20', edge_img_20)
cv2.imshow('edge_img_d', edge_img_d)
cv2.imshow('edge_img_e', edge_img_e)
cv2.waitKey(0)

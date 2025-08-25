import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.png'))
print(img.shape)

#line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (100, 150), (300, 450), (255, 0, 0), 5)

#circle
cv2.circle(img, (500, 330), 25, (0, 0, 255), 8)

#text
cv2.putText(img, "Qwerty", (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)

cv2.imshow('img', img)
cv2.waitKey(0)

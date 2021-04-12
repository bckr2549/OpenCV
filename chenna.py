import cv2
import numpy as np
input = cv2.imread('img1.jpg')
cv2.imshow('Reddy',input)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(input.shape)
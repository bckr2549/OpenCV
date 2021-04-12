import cv2
import numpy as np
image = cv2.imread('lpu.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

cv2.imshow('Adaptive mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)

if cv2.waitKey(0) & 0xf == 27:
    cv2.destroyAllWindows()
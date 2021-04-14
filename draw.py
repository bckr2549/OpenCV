import cv2
import numpy as np

blank = np.zeros((500,500), dtype = 'uint8')
cv2.imshow('Blank', blank)
img = cv2.imread('photoes/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
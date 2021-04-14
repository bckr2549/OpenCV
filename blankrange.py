import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv2.imshow('Blank', blank)

blank[200:400, 400:500] = 0,255,0
cv2.imshow('Green', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv2.imshow('Blank', blank)

cv2.rectangle(blank, (0,0), (250,250),(0,255,0), thickness=cv2.FILLED)
cv2.imshow('Rectangle',blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv2.imshow('Blank', blank)
cv2.putText(blank,'Hello, my name is krishna!!!',(0,225),cv2.FONT_HERSHEY_COMPLEX,1.0, (0,0,255),2)
cv2.imshow('Text', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
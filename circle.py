import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv2.imshow('Blank', blank)
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(0,0,250),thickness=-1) 
cv2.imshow('Circle', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
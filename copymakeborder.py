import cv2
import numpy as np
image = cv2.imread('geeks.png')
image = cv2.copyMakeBorder(image, 10, 10, 10, 10,cv2.BORDER_CONSTANT)
cv2.imshow('Border',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
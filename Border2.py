import cv2
import numpy as np
image = cv2.imread('img1.jpg')
image = cv2.copyMakeBorder(image, 100, 100, 100, 100,cv2.BORDER_REFLECT)
cv2.imshow('Border',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
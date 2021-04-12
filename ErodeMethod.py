import cv2
import numpy as np
image = cv2.imread('geeks.png')

kernel = np.ones((1,1), np.uint8)
image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
image1 = cv2.imread('input5.png')
image2 = cv2.imread('input6.png')
dest_and = cv2.bitwise_and(image2, image1, mask=None)
cv2.imshow('Bitwise_And', dest_and)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
import cv2
import numpy as np
img1 = cv2.imread('input5.png')
img2 = cv2.imread('input6.png')
dest_xor = cv2.bitwise_xor(img2, img1, mask=None)
cv2.imshow('Bitwise_xor', dest_xor)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
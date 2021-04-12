import cv2
import numpy as np

img = cv2.imread('cat_damaged.png')

mask = cv2.imread('cat_mask.png',0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('cat_inpainted',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
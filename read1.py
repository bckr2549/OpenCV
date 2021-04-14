import cv2
img = cv2.imread('photoes/cat_large.jpg')
cv2.imshow('cat_large', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
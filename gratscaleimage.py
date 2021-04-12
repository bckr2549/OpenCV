import cv2
img = cv2.imread('lpu.png',0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
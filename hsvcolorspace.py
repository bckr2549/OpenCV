import cv2
img = cv2.imread('g4g.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
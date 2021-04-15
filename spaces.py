import cv2

img = cv2.imread('photoes/lady.jpg')
cv2.imshow('Lady', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB',lab)

cv2.waitKey(0)
cv2.destroyAllWindows()
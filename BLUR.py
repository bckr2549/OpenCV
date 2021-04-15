import cv2
img = cv2.imread('photoes/lady.jpg')
cv2.imshow('Lady', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_REFLECT)
cv2.imshow('BLUR', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
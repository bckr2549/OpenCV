import cv2

img = cv2.imread('photoes/lady.jpg')
cv2.imshow('Lady', img)
#averaging
average = cv2.cv2.blur(img, (7,7))
cv2.imshow('Average_Blur', average)

gauss = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow('Gaussian Blur',gauss )

median = cv2.medianBlur(img, 7)
cv2.imshow('Median', median)

bilateral = cv2.bilateralFilter(img, 10, 15,15)
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(0)
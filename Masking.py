import cv2
import numpy as np

img = cv2.imread('photoes/lady.jpg')
cv2.imshow('Lady', img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('Blank Image', blank)

mask = cv2.circle(blank,(img.shape[1]//2 + 45,img.shape[0]//2),100,255,-1)
cv2.imshow('Mask',mask)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked Image', masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
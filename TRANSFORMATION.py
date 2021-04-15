import cv2
import numpy as np

img = cv2.imread('photoes/lady.jpg')
cv2.imshow('Lady', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x],[0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, -100)
cv2.imshow('Translated', translated)

cv2.waitKey(0)
cv2.destroyAllWindows()


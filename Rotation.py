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

def rotate(img, angle, rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2,height//2)

    rotMat = cv2.getRotationMatrix2D(rotpoint, angle,1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv2.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -60)
cv2.imshow('Rotated Rotated', rotated_rotated)

resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

cropped = img[200:400, 400:500]
cv2.imshow('Cropped',cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()


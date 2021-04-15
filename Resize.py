import cv2
img = cv2.imread('photoes/cat.jpg')
cv2.imshow('Cat', img)

resized = cv2.resize(img, (300,400), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

cropped = img[50:200, 200:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
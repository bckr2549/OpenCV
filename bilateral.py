import cv2

img = cv2.imread('taj.jpg')

bilateral = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow('taj_bilateral', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
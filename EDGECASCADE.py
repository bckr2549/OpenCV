import cv2
img = cv2.imread('photoes/park.jpg')
cv2.imshow('Park',img)

blur = cv2.GaussianBlur(img,(3,3), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)


canny = cv2.Canny(blur, 205, 255)
cv2.imshow('Canny Edges',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
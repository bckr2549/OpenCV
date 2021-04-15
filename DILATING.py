import cv2
img = cv2.imread('Photoes/lady.jpg')
cv2.imshow('Lady', img)

canny = cv2.Canny(img, 125,175)
cv2.imshow('Canny Edges', canny)

dilated = cv2.dilate(canny,(7,7), iterations=3)
cv2.imshow('Dilated', dilated)

eroded = cv2.erode(dilated, (7,7), iterations=1)
cv2.imshow('Eroded',eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
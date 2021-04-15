import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('photoes/lady.jpg')
cv2.imshow('Lady',img)
blank = np.zeros(img.shape[:2],dtype='uint8')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

circle = cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)


mask = cv2.bitwise_and(gray,gray,mask=circle)
cv2.imshow('Mask', mask)
gray_hist = cv2.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


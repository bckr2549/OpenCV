import cv2
import matplotlib.pyplot as plt

img = cv2.imread('photoes/cat.jpg')
cv2.imshow('Cat', img)

#plt.imshow(img)
#plt.show()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB',lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',rgb)

hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV_BGR',hsv_bgr)

lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB_BGR',lab_bgr)
plt.imshow(rgb)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
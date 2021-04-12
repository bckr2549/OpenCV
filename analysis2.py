import cv2
import matplotlib.pyplot as plt
img = cv2.imread('hist2.png')
plt.hist(img.ravel(),256,[0,256])
plt.show()
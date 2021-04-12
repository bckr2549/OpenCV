import matplotlib.pyplot as plt
import cv2
import numpy as np
img = cv2.imread('hist1.png',0)
histr = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(histr)
plt.show()
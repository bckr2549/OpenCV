import cv2
import numpy as np
img = cv2.imread('log.png')
for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = np.uint8)
    cv2.imshow('gamma_transformed'+str(gamma)+'.png', gamma_corrected)
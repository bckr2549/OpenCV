import cv2

img = cv2.imread('photoes/cat.jpg')
cv2.imshow('Cat', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Simple Threshold',thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Threshold Inverse',thresh_inv)

adaptive_thresh = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1)
cv2.imshow('Adaptive Threshold',adaptive_thresh)
cv2.waitKey(0)
import cv2
path = r'C:\Users\CHENNA KRISHNA\Desktop\open cv\.vscode\lpu.png'
src = cv2.imread(path)

window_name = 'Image'
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow(window_name, image)
import cv2
import numpy as np
path = r'\Users\CHENNA KRISHNA\Desktop\open cv\.vscode\geeks.png'
scr = cv2.imread(path)
window_name = 'Image'
image = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
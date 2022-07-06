import numpy as np
import cv2

img = cv2.imread('Images/guts wallpaper.png')
img = cv2.resize(img, (0, 0), fx=0.7, fy=.8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 2)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
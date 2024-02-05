import numpy as np
import cv2 as cv

capture = cv.imread("images/corners/chessfront.jpg")
capture = cv.resize(capture, (0, 0), fx=0.3, fy=0.3)
gray = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.intp(corners)
for corner in corners:
    x, y = corner.ravel()
    cv.circle(capture, (x, y), 5, (255, 0, 0), -1)
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv.line(capture, corner1, corner2, color, 1)

cv.imshow("mask", capture)
cv.waitKey(0)
cv.destroyAllWindows()

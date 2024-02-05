import numpy as np
import cv2 as cv

capture = cv.VideoCapture('objects/verduras.mp4')
args
while (1):
    ret, frame = capture.read()
    if args.algo =="KNN":
        bgGround = cv.BackgroundSubtractorKNN()
    else:
        bgGround = cv.BackgroundSubtractorMOG2()

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    mask = cv.applyColorMap(gray)
    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # lower_BLUE = np.array([10, 50, 50])
    # upper_BLUE = np.array([130, 255, 255])
    # mask_BLUE = cv.inRange(hsv, lower_BLUE, upper_BLUE)

    # lower_GREEN = np.array([40, 40, 40])
    # upper_GREEN = np.array([80, 255, 255])
    # mask_GREEN = cv.inRange(hsv, lower_GREEN, upper_GREEN)

    # lower_RED = np.array([0, 100, 100])
    # upper_RED = np.array([205, 255, 255])
    # mask_RED = cv.inRange(hsv, lower_RED, upper_RED)
    # # # save
    # # # compare
    # # # display célula, name
    # combined_masks = cv.add(mask_GREEN, mask_RED)
    # # # print(combined_masks)
    # result = cv.bitwise_and(frame, frame, mask=combined_masks)

    # cv.imshow("frame", result)
    # cv.imshow("mask", combined_masks)
    # cv.imshow("mask_RED", mask_RED)
    # cv.imshow("mask_BLUE", mask_BLUE)
    # cv.imshow("mask_GREEN", mask_GREEN)

    if cv.waitKey(30) == ord("q"):
        exit()
    if not ret:
        exit()


capture.release()
cv.destroyAllWindows()

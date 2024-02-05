import cv2 as cv
import os
from dotenv import load_dotenv
cap = cv.VideoCapture("objects/video_3.mp4", 0)
object_detector = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=4)
load_dotenv()
url = os.getenv('URL')
print(url)
# while True:
#     ret, frame = cap.read()
#     w, h, _ = frame.shape
#     # print(w, h)
#     if not ret:
#         break
#     # Extract the region of interest
#     roi = frame[w - 360 : h - 146]
#     # 1. Object Detector
#     mask = object_detector.apply(roi)
#     _, mask = cv.threshold(mask, 254, 255, cv.THRESH_BINARY)
#     contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#     for cnt in contours:
#         # Calculate area and remove the elements
#         area = cv.contourArea(cnt)
#         if area > 200:
#             # cv.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
#             x, y, w, h = cv.boundingRect(cnt)
#             cv.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             # cv.putText(
#             # roi, "roi", (x, y - 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2
#             # )
#     cv.imshow("roi", roi)
#     cv.imshow("mask", mask)
#     cv.imshow("frame", frame)
#     k = cv.waitKey(3)
#     if k == ord("q"):
#         break
cv.release()
cv.destroyAllWindows()

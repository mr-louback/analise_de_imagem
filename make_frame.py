import cv2 as cv
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="This sample demonstrates the algorithm.")
parser.add_argument("image", type=str, help="path to image file")
args = parser.parse_args()
cap = cv.VideoCapture(args.image)
i = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow("image", frame)
    if cv.waitKey(30) == ord("s"):
        cv.imwrite(f"images/objects/frame_{i}_video_3.jpg", frame)
    if cv.waitKey(30) == ord("q"):
        break
    i += 1
if not cap.isOpened():
    cap.release()
    cv.destroyAllWindows()

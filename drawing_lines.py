import numpy as np
import cv2 as cv

capture = cv.VideoCapture("videos_0/video_0.mp4")
while True:
    ret, frame = capture.read()
    w = int(capture.get(3))
    h = int(capture.get(4))

    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv.resize(frame, (0,0), fx=0.5,fy=0.5)
    # image[:height//2, :width//2] = smaller_frame
    # image[height//2:, :width//2] = cv.rotate(smaller_frame, cv.ROTATE_180)
    # image[:height//2, width//2:] = cv.rotate(smaller_frame, cv.ROTATE_180)
    # image[height//2:, width//2:] = smaller_frame
    image = cv.line(frame, (0, h), (w, 0), (255, 0, 255), 3)
    image = cv.line(frame, (0, 0), (w, h), (0, 255, 0), 10)

    image = cv.rectangle(frame, (195, 48), (276, 168), (0, 0, 255), 1)
    image = cv.circle(frame, (300, 300), 60, (255, 255, 0), 7)

    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(image, "Nei is great!", (250, h - 10), font, 1.5,(0, 0, 0), 5, cv.LINE_AA)
    cv.imshow("frame", image)
    if cv.waitKey(30) == ord("q"):
        break
capture.release()
cv.destroyAllWindows()

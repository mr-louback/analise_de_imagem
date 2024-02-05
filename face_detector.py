import cv2 as cv

# images/people/imagem_0.jpg
img = cv.VideoCapture("videos_1/video_4.mp4", 0)
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
while True:
    ret, frame = img.read()
#    gray = cv.cvtColor(frame, cv.COLOR_BAYER_BG2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        roi_gray = frame[y : y + w, x : x + w]  # [y:y+w,x:x+w]
        roi_color = frame[y : y + h, x : x + w]  # [y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for ex, ey, ew, eh in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break
cv.release()
cv.destroyAllWindows()

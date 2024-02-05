import numpy as np 
import cv2 as cv

capture = cv.VideoCapture('videos_0/video_0.mp4')
while True:
  ret, frame= capture.read()
  width = int(capture.get(3))
  height = int(capture.get(4))

  image = np.zeros(frame.shape, np.uint8)
  smaller_frame = cv.resize(frame, (0,0), fx=0.5,fy=0.5)
  image[:height//2, :width//2] = smaller_frame
  image[height//2:, :width//2] = cv.rotate(smaller_frame, cv.ROTATE_180)
  image[:height//2, width//2:] = cv.rotate(smaller_frame, cv.ROTATE_180)
  image[height//2:, width//2:] = smaller_frame
  cv.imshow('frame', image)
  if cv.waitKey(30) == ord('q'):
    break
capture.release()
cv.destroyAllWindows()
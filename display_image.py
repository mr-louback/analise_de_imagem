import cv2 as cv 
img = cv.imread( 'images/people/imagem_0.jpg')
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
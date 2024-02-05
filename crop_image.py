import cv2 as cv

img = cv.imread("images/people/imagem_0.jpg")
# print(img.shape[0] - 3)
crop = img[100:200, 300:400]
img[100:200, 350:450] = crop
cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()

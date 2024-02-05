import cv2 as cv

# images/people/imagem_0.jpg
img = cv.resize(cv.imread("images/people/imagem_0.jpg", 0), (0,0), fx=0.5, fy=0.5)

# template
template = cv.resize(cv.imread("template/people/imagem_0.png", 0), (0,0), fx=0.5, fy=0.5)
h, w = template.shape
methods = [
    cv.TM_CCOEFF,
    cv.TM_CCOEFF_NORMED,
    cv.TM_CCORR,
    cv.TM_CCORR_NORMED,
    cv.TM_SQDIFF,
    cv.TM_SQDIFF_NORMED,
]
for method in methods:
    frame = img.copy()
    match = cv.matchTemplate(frame, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    frame = cv.rectangle(frame, location, bottom_right, (255, 0, 0),2)
    # matching rectange
    cv.imshow("frame", frame)
    cv.waitKey(0)
    cv.destroyAllWindows()

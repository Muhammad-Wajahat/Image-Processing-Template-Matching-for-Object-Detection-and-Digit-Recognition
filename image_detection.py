import numpy as np
import cv2

img = cv2.resize(cv2.imread('DC_Characters.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('img.png', 0), (0, 0), fx=0.8, fy=0.8)
h, w = [100,100]

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

img2 = img.copy()
for method in methods:

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_CCORR]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 20, 5)

cv2.imshow('Match', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

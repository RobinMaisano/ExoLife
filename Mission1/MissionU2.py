import cv2
import numpy as np
import Tools
import imutils

img = cv2.imread("img\\U2_surface.pbm")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(gray, 200, 400)

contours = cv2.findContours(imgCanny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

#                                           -1 permet d'afficher tous les contours // 0 permet d'afficher que le plus gros, grâce au "sort"
imgFinale = cv2.drawContours(img, contours, 0, (255, 0, 0), 2)

cv2.imshow("img", img)
cv2.imshow("imgCanny", imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()

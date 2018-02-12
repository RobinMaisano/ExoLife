import cv2
import Tools

img = cv2.imread("img\GD61.pbm", 0)
img2 = cv2.imread("img\GD61.pbm", 0)
normalized = img

Tools.showHist(img)

cv2.normalize(normalized, normalized, 0, 255, cv2.NORM_MINMAX)

blured = Tools.medianBlur(normalized)

Tools.showHist(normalized)

Tools.showHist(blured)

cv2.imshow('Non-normalized', img2)
cv2.imshow('Normalized', normalized)
cv2.imshow('blured', blured)
cv2.waitKey(0)
cv2.destroyAllWindows()

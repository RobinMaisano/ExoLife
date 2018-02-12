import cv2
from matplotlib import pyplot as plt
import Tools

img = cv2.imread("img\Gliese 667Cc_surface.pbm", 0)

equalized = Tools.equalize(img)

cv2.imshow('Equalized', equalized)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
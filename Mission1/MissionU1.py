import Tools
import cv2
import numpy as np

img = cv2.imread("img\\U1_surface.pbm", 0)
# imgHough = cv2.imread("img\\U1_surface.pbm", 0)
imgGaussian = Tools.gaussianBlur(img)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobelLessDetails = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=7)

# edges = cv2.Canny(img, 50, 150, apertureSize=3)
# minLineLength = 50
# maxLineGap = 16
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(imgHough, (x1, y1), (x2, y2), (0, 255, 0), 2)

imgCanni = cv2.Canny(img, 100, 150)


# kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# img_prewittx = cv2.filter2D(imgGaussian, -1, kernelx)
# img_prewitty = cv2.filter2D(imgGaussian, -1, kernely)
#
# imgPrewitt = cv2.add(img_prewittx, img_prewitty)  // résultat trop peu interessant, trop de "profondeur"

Tools.showHist(img)
# normalized = Tools.normalize(img)
# equalized = Tools.equalize(img)
# Tools.showHist(equalized)

cv2.imshow('image', img)
# cv2.imshow('equalized', equalized)
cv2.imshow('laplacian', laplacian)
# cv2.imshow('prewitt', imgPrewitt)
# cv2.imshow('imgHough', imgHough)
cv2.imshow('Canni', imgCanni)
# cv2.imshow('edges', edges)
cv2.imshow('sobel', sobel)
cv2.imshow('sobelLessDetails', sobelLessDetails)
cv2.waitKey(0)
cv2.destroyAllWindows()

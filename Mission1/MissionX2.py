import Tools
import cv2
import numpy as np

img = cv2.imread("img\Gliese 581d V2.pbm", 0)
img2Cosinus = img

# Filte median 1 & 2
imgBlur = Tools.medianBlur(img)
imgBlur2 = Tools.medianBlur(imgBlur)

# Filtre Gaussien
# imgGaussian = Tools.gaussianBlur(img)     //Perte d'information importante & filtrage pas assez interessant

# Filtre moyenneur
# imgMoyenne = Tools.averageBlur(imgBlur)   //Perte d'information trop importante

# Transformée consinus discrete
imgFloat = np.float32(img2Cosinus)/255.0
imgDct = cv2.dct(imgFloat)
# img8Dct = np.uint8(imgDct)*255.0

# Placement d'un cadre noir
rows, cols = img.shape
crow, ccol = rows//2, cols//2
# imgDct[crow-30:crow+30, ccol-30:ccol+30] = 0
# imgDct[crow-50:crow+50, ccol-50:ccol+50] = 0
# img8Dct[0:70, 0:70] = 0  # Haut/Gauche
# imgDct[rows-170:rows, 0:170] = 0  # Bas/Gauche
# imgDct[rows-170:rows, cols-170:cols] = 0  # Bas/Droite
# imgDct[0:170, cols-170:cols] = 0  # Haut/Droite
# imgDct[200:rows, 0:cols] = 0
# imgDct[0:rows, 200:cols] = 0

# Transformée inverse
imgBack = cv2.idct(imgDct)
# imgBack = cv2.idct(img8Dct)

# Affichage Dct et Image modifiée
cv2.imshow('discrete', imgDct)
# cv2.imshow('discrete', img8Dct)
cv2.imshow('back', imgBack)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tools.showHist(imgBlur)
Tools.showHist(imgBlur2)    # Histogramme correct

cv2.imshow("img", img)
# cv2.imshow("imgMoyenne", imgMoyenne)
# cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgBlur2", imgBlur2)
# cv2.imshow("Gaussian", imgGaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

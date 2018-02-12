import cv2
import numpy as np
import Tools

img = cv2.imread("img\HD215497.pbm", 0)
imgNormalized = img
imgColor = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
imgSize = imgColor.shape

imgNormalized = Tools.normalize(img)

mini = np.min(img)
maxi = np.max(img)

ecart = maxi - mini
quart = ecart // 4

for i in range(0, imgSize[0]):
    for j in range(0, imgSize[1]):
        if img[i, j] < mini + quart:
            imgColor[i, j] = [0, 0, 0]
        elif img[i, j] < mini + quart*2:
            imgColor[i, j] = [0, 255, 0]
        elif img[i, j] < mini + quart*3:
            imgColor[i, j] = [0, 0, 255]
        else:
            imgColor[i, j] = [26, 140, 255]

cv2.imshow("img", img)
cv2.imshow("equalized", imgNormalized)
cv2.imshow("colored", imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()

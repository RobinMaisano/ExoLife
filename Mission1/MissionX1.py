import cv2
import numpy as np
import Tools
from matplotlib import pyplot as plt

# load("img\Asellus Secundusdat") //Unreadable
# img = cv2.imread("img\StarWars.pbm") //Too big
# img = cv2.imread("img\StarWars.png") //Too big.png
img = cv2.imread("img\StarWars2.png", 0)    # Nice

# Transformation de Fourier
imgFourierShift = Tools.fourierTransform(img)
imgAfficher = 20*np.log(np.abs(imgFourierShift))

# Transformation inverse
imgBack = Tools.fourierInverse(imgFourierShift)

# Affichage avec MatPlotLib
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(imgAfficher, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(imgBack, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

import numpy as np
import cv2
import pprint as pp

# Load an color image in grayscale
img = cv2.imread("img\Encelade_surface.pbm", 0)
maxi = 0
# mini = 256
coord = ()

imgSize = img.shape
highCoord = []

for i in range(0, imgSize[0]):
    for j in range(0, imgSize[1]):
        if img[i][j] > maxi:
            maxi = img[i][j]
            coord = (i, j)
            highCoord.append(coord)


for coordonate in highCoord:
    print(coordonate)
    img = cv2.circle(img, coordonate, 5, (0, 0, 255))

print("Valeur maximale : ", maxi)


# pp.pprint(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
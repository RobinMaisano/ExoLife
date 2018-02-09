import cv2
import numpy as np

# Faire la moyenne de l'intensité des points de l'image

img = cv2.imread("img\Mars_surface.pbm", 0)
imgSize = img.shape
height, width = img.shape
pixelSum = 0

for i in range(0, imgSize[0]):
    for j in range(0, imgSize[1]):
        pixelSum += img[i][j]

moyenne = (pixelSum/(height * width))
percent = round((moyenne/255)*100)

print("La moyenne de gaz dans l'image est de", moyenne)
print("Pourcentage de gaz dans l'image", percent, "%")

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
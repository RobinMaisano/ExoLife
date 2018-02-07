import cv2

# Delimitation ligne réseau d'eau chaude

img = cv2.imread("img\Europa_surface.pbm", 0)
imgSize = img.shape

for i in range(0, imgSize[0]):
    for j in range(0, imgSize[1]):
        if img[i][j] < 220:
            img[i][j] = 0

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
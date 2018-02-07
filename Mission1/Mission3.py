import cv2

# Delimitation ligne réseau d'eau chaude

image = cv2.imread("img\Europa_surface.pbm", 0)

def mission3taux(img):
    imgSize = img.shape
    taux = 220
    for i in range(0, imgSize[0]):
        for j in range(0, imgSize[1]):
            if img[i][j] < taux:
             img[i][j] = 0
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mission3Thresholding(img):
    imgSize = img.shape

#    img = cv2.medianBlur(img, 3) # Floutage de l'image
    cv2.imshow('image', img)
    cv2.waitKey(0)
  #  th = cv2.adaptativeThreshold(img)

#mission3taux(image)
mission3Thresholding(image)
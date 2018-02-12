import cv2

# Delimitation ligne réseau d'eau chaude image Europa

image = cv2.imread("img\Europa_surface.pbm", 0)


def mission3taux(img):
    imgSize = img.shape
    taux = 150
    for i in range(0, imgSize[0]):
        for j in range(0, imgSize[1]):
            if img[i][j] < taux:
             img[i][j] = 0
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mission3GaussianThresholding(img):

    imgSize = img.shape

    thGaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Image to charge, difference between lighter and darker px, Type of THRESH, ,
    # Zone where px will be compared, difference between two px to be considered as different
    cv2.imshow('Image', thGaussian)
    cv2.waitKey(0)


def mission3MeanThresholding(img):

    imgSize = img.shape

    thMean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # Image to charge, difference between lighter and darker px, Type of THRESH, ,
    # Zone where px will be compared, difference between two px to be considered as different
    cv2.imshow('Image', thMean)
    cv2.waitKey(0)

# mission3taux(image)
mission3GaussianThresholding(image)
# mission3MeanThresholding(image)

import cv2
from matplotlib import pyplot as plt


def medianBlur(image):
    # Application d'un filtre median dans une range de 3 cases
    image = cv2.medianBlur(image, 3)
    return image


def equalize(image):
    # Egalisation d'un histogramme
    equalized = cv2.equalizeHist(image)
    return equalized


def normalize(image):
    # Normalisation de l'image
    normalized = image
    cv2.normalize(normalized, normalized, 0, 255, cv2.NORM_MINMAX)
    return normalized


def showHist(image):
    # Affichage de l'histogramme de l'image
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

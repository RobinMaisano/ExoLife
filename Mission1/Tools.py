import cv2
import numpy as np
from matplotlib import pyplot as plt


def binaryFilter(image, k):
    # Permet de convertir une image en binaire inversée
    imgSize = image.shape
    for i in range(0, imgSize[0]):
        for j in range(0, imgSize[1]):
            if image[i, j] > k:
                image[i, j] = 255
            else:
                image[i, j] = 0
    return image


def averageBlur(image):
    # Application d'un filtre moyenneur
    filtred = cv2.blur(image, (3, 3))
    return filtred


def gaussianBlur(image):
    # Application d'un filtre gaussien
    filtred = cv2.GaussianBlur(image, (3, 3), 0)
    return filtred


def medianBlur(image):
    # Application d'un filtre median dans une range de 3 cases
    filtred = cv2.medianBlur(image, 3)
    return filtred


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


def fourierTransform(image):
    # Transformation d'une image en une transformée de Fourier
    f = np.fft.fft2(image)
    imgShift = np.fft.fftshift(f)
    return imgShift


def fourierInverse(imageShift):
    # Inversion d'une transformée de Fourier
    img2Transform = np.fft.ifftshift(imageShift)
    imgBack = np.fft.ifft2(img2Transform)
    imgBack = np.abs(imgBack)
    return imgBack
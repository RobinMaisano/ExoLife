import cv2
import numpy as np
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
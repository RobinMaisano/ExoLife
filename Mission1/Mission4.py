import cv2

img1 = cv2.imread("img\Jupiter1.pbm", 0)
img2 = cv2.imread("img\Jupiter2.pbm", 0)

def medianBlur(image):

    # Application d'un filtre median dans une range de 3 cases autour
    image = cv2.medianBlur(image, 3)

    cv2.imshow('jupiterMedian', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


medianBlur(img1)

#medianBlur(img2)
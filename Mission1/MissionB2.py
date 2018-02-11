import cv2
from matplotlib import pyplot as plt
img = cv2.imread("img\GD61.pbm", 0)
img2 = cv2.imread("img\GD61.pbm", 0)

# Histogramme avant
plt.hist(img.ravel(), 256, [0,256])
plt.show()
normalized = img

cv2.normalize(normalized, normalized, 0, 255, cv2.NORM_MINMAX)

# Histogramme apres
plt.hist(normalized.ravel(), 256, [0,256])
plt.show()

cv2.imshow('Normalized', normalized)
cv2.imshow('Non-normalized', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
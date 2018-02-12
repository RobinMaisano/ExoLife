import cv2
import Tools

img1 = cv2.imread("img\Jupiter1.pbm", 0)
img2 = cv2.imread("img\Jupiter2.pbm", 0)

result = Tools.medianBlur(img1)

# result = Tools.medianBlur(img2)

cv2.imshow('jupiterMedian', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
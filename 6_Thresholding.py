import cv2

img = cv2.imread('book.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(img1, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('ADAthreshold', gaus)
cv2.imwrite('6.1_threshold(binaryFromRGB).jpg', threshold)
cv2.imwrite('6.2_threshold(binaryFromGRAY).jpg', threshold2)
cv2.imwrite('6.3_threshold(AdaptiveGaussianFromGray).jpg', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


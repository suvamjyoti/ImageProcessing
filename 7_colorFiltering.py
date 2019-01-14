import cv2
import numpy as np
frame = cv2.imread('green.jpg')
img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([50, 151, 24])
upper_yellow = np.array([255, 255, 255])

mask = cv2.inRange(img, lower_yellow, upper_yellow)
res = cv2.bitwise_and(img, img, mask=mask)
# smoothing using gaussian blur
# blur = cv2.GaussianBlur(res, (5, 5), 0)

# median blur
# median = cv2.medianBlur(res, 15)

# bilateral blur
bilateral = cv2.bilateralFilter(res, 15, 75, 75)

# smoothing using normal blur
# further smoothing the bilateral
kernel = np.ones((3, 3), np.float32)/9
smoothed = cv2.filter2D(bilateral, -1, kernel)

# mask
cv2.imshow("mask", mask)

# result
cv2.imshow("res", res)

# result after gaussian blur
# cv2.imshow("gaussian blur", blur)\

# median blur
# cv2.imshow("resAfterMedian", median)

# bilateral blur
cv2.imshow("resAfterBilateral", bilateral)

# result after normal blur
cv2.imshow("resAfterSmoothingTheBilateral", smoothed)

cv2.waitKey(0)
cv2.imwrite("7.1_colorFiltering(hsv).jpg", img)
cv2.imwrite("7.2_colorFiltering(mask).jpg", mask)
cv2.imwrite("7.3_colorFiltering(res).jpg", res)
cv2.imwrite("7.4_colorFiltering(resAfterBilateralBlur).jpg", bilateral)
cv2.imwrite("7.5_colorFiltering(BestResult).jpg", smoothed)
cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 5)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, 255, -1)


cv2.imshow("window", img)
cv2.waitKey(0)
cv2.imwrite("11_cornerDetection.jpg", img)
cv2.destroyAllWindows()
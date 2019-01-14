import numpy as np
import cv2

# reading image
img = cv2.imread('cube.jpg')

i = 0
j = 0

# i denotes height
# j denotes width

for i in range(360):
    for j in range(480):
        a = img[i, j]
        # required color
        b = [0, 0, 255]

        # checking difference in redness of a pixel by using distance formula
        dist = np.linalg.norm(a-b)
        if dist < 150:
            img[i, j] = [255, 255, 255]
        else:
            img[i, j] = img[i, j]


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('5_img_arithmatic.jpg', img)
cv2.destroyAllWindows()
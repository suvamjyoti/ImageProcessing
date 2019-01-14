import numpy as np
import cv2

img = cv2.imread('cube.jpg', 1)

# changing a pixel color value
img[295, 295] = [255, 255, 255]

# changing the color of  a block of image
img[250:275, 250:275] = [255, 255, 255]

# coping and pasting the roi(region of image) at different place
roi = img[200:300, 200:300]
img[0:100, 0:100] = roi

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('4_img_analysis.jpg', img)
cv2.destroyAllWindows()

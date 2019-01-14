import cv2


img = cv2.imread('cube.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('1_first.jpg', img)
cv2.destroyAllWindows()



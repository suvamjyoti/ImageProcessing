import cv2
import numpy as np

image = cv2.imread('image.jpg')
img_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_bgr, template, cv2.TM_CCOEFF_NORMED)
res1 = cv2.cvtColor(res, cv2.COLOR_GRAY2BGR)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 1)

# result
cv2.imshow("template", image)
cv2.imshow("RES", res)
cv2.waitKey(0)
cv2.imwrite('9_templateMatching(res).jpg', image)
cv2.destroyAllWindows()
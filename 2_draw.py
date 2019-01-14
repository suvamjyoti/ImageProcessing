import cv2
import numpy as np

img = cv2.imread('cube.jpg', 1)

# line
cv2.line(img, (0, 0), (210, 220), (0, 0, 255), 5)

# rectangle
cv2.rectangle(img, (150, 100), (350, 200), (255, 0, 0), 5)

# circle
cv2.circle(img, (200, 200), 100, (0, 255, 0), 5)

# polygon
pts = np.array([[0, 25], [140, 210], [230, 20], [350, 350]], np.int32)
cv2.polylines(img, [pts], True, (255, 100, 255), 5)

# write
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'open cv Test !', (0, 130), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite("2_draw.jpg", img)
cv2.destroyAllWindows()

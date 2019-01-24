import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blue(cyan)
    # LowerRange
    lower = np.array([100, 140, 0])
    # UpperRange
    upper = np.array([200, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    # smoothingMask
    smooth = cv2.medianBlur(mask, 5)

    # morphologicalTransformation
    # bigger the matrix bigger the effect
    kernel = np.ones((4, 4), np.uint8)  # for erosion
    kernel1 = np.ones((7, 7), np.uint8)  # for dilation
    # erosion = A pixel in the original image (either 1 or 0) will be considered 1
    # only if all the pixels under the kernel is 1,
    # otherwise it is eroded (made to zero).
    erosion = cv2.erode(mask, kernel, iterations=1)
    # dilation = a pixel element is '1' if at least one pixel under the kernel is '1
    dilation = cv2.dilate(erosion, kernel1)  # we are actually performing closing(dilation followed by erosion)

    # result
    res = cv2.bitwise_and(hsv, hsv, mask=mask)
    res1 = cv2.bitwise_and(hsv, hsv, mask=erosion)
    res2 = cv2.bitwise_and(hsv, hsv, mask=dilation)

    # viewing screens
    cv2.imshow('res', res)
    cv2.imshow('res after erosion', res1)
    cv2.imshow('res after closing', res2)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
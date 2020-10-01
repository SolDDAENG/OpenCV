import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))  # 가장 큰 픽셀이 100 픽셀이 되도록 계산하는 수식. => 픽셀의 최대값이 100이 넘지 않도록 한다.
        cv2.line(imgHist, pt1, pt2, 0)  # line()함수로 히스토그램 그래프를 그린다. pt1부터 시작해서 pt2까지. pt1: y가 0인 x좌표. pt2: y값이 있는 x좌표 => x좌표를 기준으로 세로로 선을 그린다.

    return imgHist


src = cv2.imread('ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()

cv2.destroyAllWindows()

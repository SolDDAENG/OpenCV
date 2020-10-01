# 히스토그램 분석

# 히스토그램 (Histogram)
# 영상의 픽셀 값 분포를 그래프의 형태로 표현한 것
# 예를 들어 그레이스케일 영상에서 각 그레이스케일 값에 해당하는 픽셀의 개수를 구하고, 이를 막대 그래프의 형태로 표현

# 정규화된 히스토그램 (Normalized histogram)
# ex) 크기가 서로 다른 경우 크기에 대해 정규화를 해서 정규화된 히스토그램을 계산
# 각 픽셀의 개수를 영상 전체 픽셀 개수로 나누어준 것
# 해당 그레이스케일 값을 갖는 픽셀이 나타날 확률

# 히스토그램 구하기
# cv2.calcHist(imags, channels, mask, histSize, ranges, hist=None, accumulate=None) -> hist
# images : 입력 영상 리스트 (리스트로 담아줘야 한다. 한 장의 영상인 경우에도 리스트로 묶어줘야 한다.)
# channels : 히스토그램을 구할 채널을 나타내는 리스트. grayscale : [0], color : [0, 1, 2]-(bgr), [0, 1]-(bg)
# mask : 마스크 영상. 입력 영상 전체에서 히스토그램을 구하려면 None 지정.
# histSize : 히스토그램 각 차원의 크기(빈(bin)의 개수)를 나타내는 리스트  # [256] : grayscale. [128] : 픽셀값이 0 또는 1, 2 또는 3, 4 또는 5인 것
# ranges : 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트  # (범위) [0, 256], [0, 256, 0, 256]
# hist : 계산된 히스토그램(numpy.ndarray)
# accumulate : 기존의 hist 히스토그램에 누적하려면 True, 새로 만들려면 False. 기본값은 False.


import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


# 그레이스케일 영상의 히스토그램
src = cv2.imread('ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist)
plt.show()

# 컬러 영상의 히스토그램
src = cv2.imread('ch03/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()

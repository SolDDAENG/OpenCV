# 특정 색상 영역 추출

# RGB 색 공간에서 녹색 영역 추출하기
# ex) 0 < R < 100, 128 < G < 255, 0 < B < 100
# 영상의 밝기 정도에 따라 정확한 추출히 안되는 경우도 있다.

# HSV 색 공간에서 녹색 영역 추출하기
# 50 < H(색상) < 80, 150 < S(색상(녹색)의 정도) < 255, 0 < V(밝기) < 255
# 영상의 밝기 정도에 상관없이 추출이 잘된다.

# 특정 범위 안에 있는 행렬 원소 검출
# cv2.inRange(src, lowerb, upperb, dst=None) -> dst
# src : 입력 행렬
# lowerb : 하한 값 행렬 또는 스칼라
# upperb : 상한 값 행렬 스칼라
# dst : 입력 영상과 같은 크기의 마스크 영상. (numpy.uint8)
#     : 범위 안에 들어가는 픽셀은 255, 나머지는 0으로 설정.


import sys
import numpy as np
import cv2


# src = cv2.imread('candies.png')
src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))  # B : 0 ~ 100, G : 128 ~ 255, R : 0 ~ 100
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))  # H : 50 ~ 80, S : 150 ~ 255, V : 0 ~ 255

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()

# 잡음 제거(2) : 양방향 필터
# 가우시안 잡음 제거에는 가우시안 필터가 효과적. 다만, 원본 영상의 edge정보도 깎이는 단점이 있다.

# 양방향 필터 (Bilateral filter)
# edge 보전 잡음 제거 필터(edge-preserving noise removal filter)의 하나
# 평균값 필터 또는 가우시안 필터는 edge 부근에서도 픽셀값을 평탄하게 만드는 단점이 있다.
# 기준 픽셀과 이웃 픽셀과의 거리, 그리고 픽셀 값의 차이를 함계 고려하여 블러링 정도를 조절

# 양방향 필터링 함수 -> 연산 속도가 조금 오래 걸린다. -> 너무 오래 걸린땐 sigma값을 조정하기
# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None) -> dst
# src : 입력 영상. 8비트 또는 실수형, 1채널 또는 3채널.
# d : 필터링에 사용될 이웃 픽셀의 거리(지름).
#   : 음수(-1)를 입력하면 sigmaSpace 값에 의해 자동 결정됨. => -1을 주는 것이 좋다.
# sigmaColor : 색 공간에서 필터의 표준 편차. => edge인지 아닌지를 판단하기 위한 기준값.
# sigmaSpace : 좌표 공간에서 필터의 표준 편차.
# dst : 출력 영상. src와 같은 크기, 같은 타입.
# borderType : 가장가리 픽셀 처리 방식


import sys
import numpy as np
import cv2

# src = cv2.imread('ch04/lenna.bmp')
src = cv2.imread('ch04/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)
# dst = cv2.bilateralFilter(src, -1, 100, 50)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

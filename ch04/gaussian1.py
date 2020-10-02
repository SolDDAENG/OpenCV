# 블러링(2) : 가우시안 필터

# 평균값 필터에 의한 블러링의 단점 -> 결과 영상의 퀄리티 면에서 썩 좋은 방법은 아니다.
# 필터링 대상 위치에서 가까이 있는 픽셀과 멀리 있는 픽셀이 모두 같은 가중치를 사용하여 평균을 계산
# 멀리 있는 픽셀의 영향을 많이 받을 수 있다

# (1차원) 가우시안 함수 (Gaussian function) : 정규분포
# 특징 : 평균 주위의 대칭 (종형 곡선) 모양. mean = median(중앙값) = mode = 가장 높은 값. area under the curve = 1

# 2차원 가우시안 함수(μx = μy = 0, σx = σy = σ)
# Gσ(x, y) = (1 / 2 * π * σ^2 * e)^(-(x^2 + y^2) / 2σ^2)
# 2차원 가우시안 필터 마스크 크기 (σ = 1.0)
# 필터 마스크 크기 : (8σ + 1) : float 또는 (6σ + 1) : uint8

# 가우시안 필터링 함수
# cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None) -> dst
# src : 입력 영상. 각 채널 별로 처리됨.
# dst : 출력 영상. src와 같은 크기, 같은 타입
# ksize : 가우시안 커널 크기. (0, 0)을 지정하면 sigma 값에 의해 자동 결정됨. => 가급적이면 (0, 0)을 주는것이 좋다.
# sigmaX : x방향 sigma. (x방향의 표준편차)
# sigmaY : y방향 sigma. 0이면 sigmaX와 같게 설정. 가급적이면 0이나 None을 주는것을 추천
# borderType : 가장자리 픽셀 확장 방식.


import sys
import numpy as np
import cv2


src = cv2.imread('ch04/rose.bmp', cv2.IMREAD_GRAYSCALE)

# dst = cv2.GaussianBlur(src, (0, 0), 1)
dst = cv2.GaussianBlur(src, (0, 0), 2)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()

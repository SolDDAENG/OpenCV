# 케니 에지 검풀

# 좋은 에지 검풀기의 조건
# 정확한 검풀(Good detection) : 에지가 아닌 점을 에지로 찾거나 또는 에지인데 에지로 찾지 못하는 확률을 최소화
# 정확한 위치(Good Localization) : 실제 에지의 중심을 검출
# 단일 에지(Single edge) : 하나의 에지는 하나의 점(픽셀)으로 표현

# 캐니 에지 검출
# 1단계
# 가우시안 필터링 - (Optional) 잡음 제거 목적

# 2단계
# 그래디언트계산 - 주로 소벨마스크를 사용

# 3단계
# 비최대억제(Non-maximumsuppression)
# 하나의 에지가 여러개의 픽셀로 표현되는 현상을 없애기 위하여 그래디언트 크기가 국지적 최대 (local maximum)인 픽셀만을 에지 픽셀로 설정
# 그래디언트 방향에 위치한 두 개의 픽셀을 조사하여 국지적 최대를 검사

# 4단계
# 히스테리시스 에지 트래킹(Hysteresis edge tracking)
# 두 개의 임계값을 사용: 𝑇𝐿𝑜𝑤 , 𝑇𝐻𝑖𝑔h
# 강한에지 : ||𝑓|| ≥ 𝑇𝐻𝑖𝑔h → 최종 에지로 선정 - Strong edge
# 약한에지 : 𝑇𝐿𝑜𝑤 ≤ ||𝑓|| < 𝑇𝐻𝑖𝑔h → 강한 에지와 연결되어 있는 픽셀만 최종 에지로 선정 - Weak edge

# 캐니 에지 검출 함수
# cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None) -> edges
# image : 입력 영상
# threshold1 : 하단 임계값  # threshold1 : threshold2  1:2 또는 1:3 => 꼭 이 값은 아니고 적당히 주면 된다.
# threshold2 : 상단 임계값
# edges : 에지 영상
# apertureSize : 소벨 연산을 위한 커널 크기. 기본값은 3.
# L2gradient : True이면 L2 norm 사용, False이면 L1 norm 사용. 기본값은 False.  L2가 더 정확하지만 L1보다 속도가 느리다.


import sys
import numpy as np
import cv2


src = cv2.imread('ch06/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)  # Canny()함수에 컬러영상을 줄 수도 있지만 그레이스케일이 일반적이다. 컬러 영상의 경우 RGB 3개의 채널을 따로따로 canny를 검출해서 그 중 최대값을 선택
# dst = cv2.Canny(src, 100, 150)
# dst = cv2.Canny(src, 150, 200)

cv2.imshow('src', src)
cv2.imshow('dst1', dst)
cv2.waitKey()

cv2.destroyAllWindows()

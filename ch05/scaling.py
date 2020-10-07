# 영상의 확대와 축소

# 크기 변환(Scale transformation)
# 영상의 크기를 원본 영상보다 크게 또는 작게 만드는 변환
# x축과 y축 방향으로의 스케일 비율(scale factor)를 지정

# 영상의 크기 변환
# cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None) -> dst
# src : 입력 영상
# dsize : 결과 영상 크기. (w,h)튜플. (0,0)이면 fx와 fy 값을 이용하여 결정.
# dst : 출력 영상
# fx, fy : x와 y 방향 스케일 비율(scale factor). dsize 값이 0일 때 유효. 똑같은 크기 : 1, 1, 두 배로 키우려면 2, 2, 축소하려면 0.5, 0.5
# interpolation : 보간법 지정. 기본값은 cv2.INTER_LINEAR
#   cv2.INTER_NEAREST : 최근방 이웃 보간법 - 가장 빠르게 동작하지만 결과 영상의 품질이 좋지 않다.
#   cv2.INTER_LINEAR : 양선형 보간법 (2x2 이웃 픽셀 참조) - 어느정도 퀄리티가 괜찮고 속도가 빠르다.
#   cv2.INTER_CUBIC : 3차회선 보간법 (4x4 이웃 픽셀 참조) - INTER_LINEAR보다 품질이 좋지만 속도가 조금 느리다.
#   cv2.INTER_LANCZOS4 : Lanczos 보간법 (8x8이웃 픽셀 참조) - 좀 더 복잡하고 시간은 더 오래 걸리지만 퀄리티는 위보다 조금 더 좋다.
#   cv2.INTER_AREA : 영상 축소 시 효과적 - 영역적인 정보를 추출해서 결과영상의 픽셀값을 셋팅한다.

# 영상의 축소 시 고려할 사항
# 영상 축소 시 디테일이 사라지는 경우가 발샐 (e.g. 한 픽셀로 구성된 선분)
# 입력 영상을 부드럽게 필터링한 축소, 다단계 축소
# OpenCV의 cv2.resize() 함수에서는 cv2.INTER_AREA 플래그를 사용

# 영상의 대칭 변환(flip, reflection)
# cv2.flip(src, flipCode, dst=None) -> dst
# src : 입력 영상
# flipCode : 대칭 방향 지정
#   양수(+1) : 좌우 대칭
#   0 : 상하 대칭
#   음수(-1) : 좌우 & 상하 대칭
# dst : 출력 영상

import sys
import numpy as np
import cv2


src = cv2.imread('ch05/rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)  # fx=4, fy=4 ==> (1920, 1280)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

flp1 = cv2.flip(src, 1)
flp2 = cv2.flip(src, 0)
flp3 = cv2.flip(src, -1)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.imshow('flp1', flp1)
cv2.imshow('flp2', flp2)
cv2.imshow('flp3', flp3)
cv2.waitKey()
cv2.destroyAllWindows()

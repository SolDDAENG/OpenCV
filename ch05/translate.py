# 영상의 이동 변환

# 영상의 기하학적 변환(geometric transformation)이란? -> 픽셀의 좌표가 다른 좌표로 이동.
# 영상을 구성하는 픽셀의 배치 구조를 변경함으로써 전체 영상의 모양을 바꾸는 작업
# Image registration, removal of grometric fistortion, etc.

# 이동 변환(Translation transformation)
# 가로 또는 세로 방향으로 영상을 특정 크기만큼 이동시키는 변환
# x축과 y축 방향으로의 이동 변위를 지정

# 영상의 어파인 변환 함수
# cv2.warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None) -> dst
# src : 입력 영상
# M : 2x3 어파인 변환 행렬. 실수형.
# dsize : 결과 영상 크기. (w,h)튜플. (0,0)이면 src와 같은 크기로 설정.
# dst : 출력 영상
# flags : 보간법. 기본값은 v2.INTER_LINEAR
# borderMode : 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
# borderValue : cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0. => 변환하면 새로운 공간들이 생겨난다 
#               -> 이때 0을 입력하면 RGB성분이 검정색으로 채워짐. 255로 셋팅하면 흰색으로 채워짐


import sys
import numpy as np
import cv2


src = cv2.imread('ch05/tekapo.bmp')  # 640x480

if src is None:
    print('Image load failed!')
    sys.exit()

# 가로 200픽셀, 세로 100 픽셀 이동
# 어파인 변환 행렬을 먼저 만들어야 한다.
aff = np.array([[1, 0, 200], [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

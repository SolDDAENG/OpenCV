# 잡음제거(1) : 미디언 필터

# 영상의 잡음(Noise)
# 영사의 픽셀 값에 추가되는 원치 않는 형태의 신호
# f(x,y) = s(x,y) + n(x,y)
# f : 획득된 영상, s : 원본 신호, n : 잡음

# 잡음의 종류
# 가우시안 잡음 (Gaussian noise) - 지금은 대부분 가우시안 잡음이다.
# 소금 & 후추 잡음 (Salt & Pepper) - 아날로그에서 많이 보이는 잡음. 요즘에는 보기 힘들다.

# 미디언 필터 (Median filter) - 요즘엔 많이 사용되진 않는다.
# 주변 픽셀들의 값들을 정렬하여 그 중앙값(median)으로 픽셀 값을 대체
# 소금-후추 잡음 제거에 효과적

# 미디언 필터링 함수
# cv2.medianBlur(src, ksize, dst=None) -> dst
# src : 입력 영상. 각 채널 별로 처리됨.
# ksize : 커널 크기. 1보다 큰 홀수를 지정.
# dst : 출력 영상. src와 같은 크기, 같은 타입.


import sys
import numpy as np
import cv2

src = cv2.imread('ch04/noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3)  # ksize가 클수록 더 뭉친 결과가 출력된다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

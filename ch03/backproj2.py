# 히스토그램 역투영을 이용한 살색 검출
# 1) 기준 영상으로부터 살색에 대한 컬러 히스토그램을 미리 계산
# 2) 입력 영상에서 미리 구한 살색 히스토그램에 부합하는 픽셀을 선별

import sys
import numpy as np
import cv2


# CrCb 살색 히스토그램 구하기
ref = cv2.imread('kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)  # 입력 영상 전체에서 히스토그램을 구하고 싶으면 None, 특정 영역에서만 히스토그램을 구하고싶으면 mask.
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255,  # hist의 가장 큰 값들은 너무 큰 값들이 나오기 때문에 log를 해주는 것이 좋다. hist가 0일 수도 있기 때문에 hist + 1을 해준다.
                          cv2.NORM_MINMAX, cv2.CV_8U)  # 2차원 형태의 hist를 그레이스케일 영상으로 변환

# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()

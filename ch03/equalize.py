# 히스토그램 평활화

# 히스토그램 평활화(Histogram equalization)
# 히스토그램이 그레이스케일 전체 구간에서 균일한 분포로 나타나도록 변경하는 명암비 향상 기법
# 히스토그램 균등화, 균일화, 평탄화

# 히스토그램 평활화
# cv2.equalizeHist(src, dst-None) -> dst
# src : 입력영상. 그레이스케일 영상만 가능.
# dst : 결과 영상

# 컬러 히스토그램 평활화
# 직관적 방법 : R, G, B 각 색 평면에 대해 히스토그램 평활화 => 색감이 완전히 변해버리는 경우가 발생한다.
# 밝기 성분에 대해서만 히스토그램 평활화 수행 (색상 성분은 불변) - YCrCb 이용


import sys
import numpy as np
import cv2


# 그레이스케일 영상의 히스토그램 평활화
src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 컬러 영상의 히스토그램 평활화
src = cv2.imread('field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
planes = cv2.split(src_ycrcb)

# 밝기 성분에 대해서만 히스토그램 평활화 수행
planes[0] = cv2.equalizeHist(planes[0])  # 밝기 성분만 보정
dst_ycrcb = cv2.merge(planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)  # 다시 BGR로 변환을 해줘야 한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

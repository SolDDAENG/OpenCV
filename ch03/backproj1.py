# 히스토그램 역투영(Histogram backprojection)
# 영상의 각 픽셀이 주어진 히스토그램 모델에 얼마나 일치하는지를 검사하는 방법
# 임의의 색상 영역을 검출할 때 효과적

# 히스토그램 역투영 함수
# cv2.calcBackProject(images, channels, hist, ranges, scale, dst=None) -> dst
# images : 입력 영상 리스트
# channels : 역투영 계산에 사용할 채널 번호 리스트
# hist : 입력 히스토그램 (numpy.ndarray)
# ranges : 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
# scale : 출력 역투영 행렬에 추가적으로 곱할 값. 곱할 값이 없으면 1.
# dst : 출력 역투영 영상. 입력 영상과 동일한 크기. cv2.CV_8U => 그레이스케일. 
#     : 히스토그램에 아주 부합할수록 255에 가까운 값. 전혀 부합하지 않으면 0.

import sys
import numpy as np
import cv2


# 입력 영상에서 ROI를 지정하고, 히스토그램 계산
src = cv2.imread('cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()

x, y, w, h = cv2.selectROI(src)  # 마우스로 영역 선택

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w]  # 사용자가 선택한 사각형 영역의 부분 영상

channels = [1, 2]  # Y성분인 0번 채널은 그레이스케일이고 밝기 정보이고 때문에 조명의 영향을 무시하기 위해 사용하지 않는다.
cr_bins = 128  # 256을 써야하지만 128을 써서 단순화시킴. 결과는 비슷하다.
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256]  # 0 ~ 255
cb_range = [0, 256]
ranges = cr_range + cb_range  # [0, 256, 0, 256]

hist = cv2.calcHist([crop], channels, None, histSize, ranges)  # 히스토그램 계산
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대해 히스토그램 역투영
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

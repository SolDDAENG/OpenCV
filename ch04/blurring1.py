# 영상의 필터링(image filtering)
# 영상에서 필요한 정보만 통과시키고 원치 않는 정보는 걸러내는 작업

# 공간적 필터링 (Spatial domain filtering)
# 영상의 픽셀 값을 직접 이용하는 필터링 방법
# - 대상 좌표의 픽셀 값과 주변 픽셀 값을 동시에 사용
# 주로 마스크(mask)연산을 이용함
# (마스크 = 커널(kernel) = 윈도우(window) = 템플릿(template))  # 마스크 = 커널 = 작은 크기의 실수형 행렬

# 필터링 : 마스크 연산  ==> Correlation (Convolution)
# 다양한 모양과 크기의 마스크 (Anchor : 고정점. 필터링을 하고자 하는 대상 픽셀의 위치. 대부분 필터의 정중앙에 위치.)
# 마스크의 형태와 값에 따라 필터의 역활이 결정됨
# - 영상 부드럽게 만들기
# - 영상 날카롭게 만들기
# - 에지(edge) 검출
# - 잡음 제거

# 기본적인 2D 필터링
# cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None) -> dst
# src : 입력 영상
# ddepth : 출력 영상 데이터 타입. (e.g.) cv2.CV_8U, cv2.CV_32F, cv2.CV_64F
#        : -1을 지정하면 src와 같은 타입의 dst 영상을 생성
# kernel : 필터 마스크 행렬. 실수형.
# anchor : 고정점 위치. (-1, -1)이면 필터 중앙을 고정점으로 사용
# delta : 추가적으로 더할 값. 기본값은 0
# borderType : 가장자리 픽셀 확장 방식
# dst : 출력 영상

# 블러링(1) : 평균값 필터(Mean filter)
# 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
# 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 에지가 무뎌지고, 영상에 있는 잡음의 영향이 사라지는 효과

# 평균값 필터링 함수
# cv2.blur(src, ksize, dst=None, anchor=None, borderType=None) -> dst
# src : 입력 영상
# ksize : kernel size. 평균값 필터 크기. (width, height) 형태의 튜플
# dst : 결과 영상. 입력의 영상과 같은 크기 & 같은 타입.


import sys
import numpy as np
import cv2


src = cv2.imread('ch04/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
'''
kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]], dtype=np.float64)
'''
# kernel = np.ones((3, 3), dtype=np.float64) / 9.
# dst = cv2.filter2D(src, -1, kernel)
dst = cv2.blur(src, (3, 3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

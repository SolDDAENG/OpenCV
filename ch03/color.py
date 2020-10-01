# 컬러 영상 처리와 색 공간

# OpenCV와 컬러 영상
# • 컬러 영상은 3차원 numpy.ndarray로 표현. img.shape = (h, w, 3)
# • OpenCV에서는 RGB 순서가 아니라 BGR 순서를 기본적으로 사용

# OpenCV에서 컬러 영상 다루기
# img1 = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
# img2 = np.zeros((480, 640, 3), np.uint8)
# img3 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)  # grayscale을 cvtColor()함수를 이용해 컬러영상으로 변환
# img4 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR) => 이 경우 img4영상의 각 픽셀은 B,G,R 색 성분 값이 모두 같게 설정됨.

# RGB 색 공간
# • 빛의 삼원색인 빨간색(R), 녹색(G), 파란색(B)를 혼합하여 색상을 표현 (가산 혼합)
# • TV & 모니터, 카메라 센서 Bayer 필터, 비트맵

# (색상) 채널 분리 => B, G, R을 분리하면 각각의 B, G, R 성분은 Grayscale 영상 형태가 된다.
# cv2.split(m, mv=None) => dst
# m : 다채널 영상 (e.g.) (B, G, R)로 구성된 컬러 영상
# mv : 출력 영상
# dst : 출력 영상 리스트

# (색상) 채널 결합
# cv2.merge(mv, dst=None) -> dst
# mv : 입력 영상 리스트 또는 튜플
# dst : 출력 영상

# 색공간변환
# • 영상 처리에서는 특정한 목적을 위해 RGB 색 공간을 HSV, YCrCb, Grayscale 등의
# • 다른 색 공간으로 변환하여 처리 • OpenCV색공간변환방법
#   https://docs.opencv.org/master/de/d25/imgproc_color_conversions.html 참고

# 색 공간 변환 함수
# cv2.cvtColor(src, code, dst=None, dstCn=None) -> dst
# src : 입력 영상
# code : 색 변환 코드
#      : cv2.COLOR_BGR2GRAY / cv2.COLOR_GRAY2BGR : BGR <-> GRAY
#      : cv2.COLOR_BGR2RGB / cv2.COLOR_RGB2BGR : BGR <-> RGB
#      : cv2.COLOR_BGR2HSV / cv2.COLOR_HSV2BGR : BGR <-> HSV
#      :cv2.COLOR_BGR2YCrCb / cv2.COLOR_YCrCb2BGR : BGR <-> YCrCb
# dstCn : 결과 영상의 채널 수. 0이면 자동 결정.
# dst : 출력 영상

# RGB 색상을 그레이스케일로 변환
# Y = 0.299R + 0.587G + 0.114B  # 대략 3:6:1 비율 => 중요도가 G > R > B 순서이다.
# • 장점 : 데이터 저장 용량 감소, 데이터 처리 속도 향상
# • 단점 : 색상 정보 손실

# HSV 색 공간
# • Hue : 색상, 색의 종류 (각도)
# • Saturation : 채도, 색의 탁하고 선명한 정도. (0 ~ 1 또는 0 ~ 255)
# • Value : 명도, 빛의 밝기 (0 ~ 1 또는 0 ~ 255)

# HSV 값 범위
# • cv2.CV_8U 영상의 경우
# ▪ 0 ≤ 𝐻 ≤ 179  (8비트에선 360까지 표현하기 못하기 때문에 360을 반으로 나눈 값으로 표현)
# ▪ 0 ≤ 𝑆 ≤ 255
# ▪ 0 ≤ 𝑉 ≤ 255

# YCrCb 색 공간
# • PAL, NTSC, SECAM 등의 컬러 비디오 표준에 사용되는 색 공간
# 영상의 밝기 정보와 색상 정보를 따로 분리하여 부호화 (흑백 TV 호환)
# Y : 밝기 정보(luma)
# Cr, Cb : 색차(chroma)

# YCrCb 값 범위
# • cv2.CV_8U 영상의 경우
# ▪ 0 ≤ 𝑌 ≤ 255
# ▪ 0 ≤ 𝐶𝑟 ≤ 255
# ▪ 0 ≤ 𝐶𝑏 ≤ 255


import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('ch03/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색 평면 분할
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
planes = cv2.split(src_hsv)
# planes = cv2.split(src)
# b_plane, g_plane, r_plane = cv2.split(src)


#b_plane = src[:, :, 0]
#g_plane = src[:, :, 1]
#r_plane = src[:, :, 2]

cv2.imshow('src', src)
cv2.imshow('planes[0]', planes[0])
cv2.imshow('planes[1]', planes[1])
cv2.imshow('planes[2]', planes[2])
# cv2.imshow('B_plane', b_plane)
# cv2.imshow('G_plane', g_plane)
# cv2.imshow('R_plane', r_plane)
cv2.waitKey()

cv2.destroyAllWindows()

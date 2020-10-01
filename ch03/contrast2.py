# 영상의 명암비 조절

# 히스토그램 스트레칭(Histogram stretching) - 영상의 특징을 분석해서 자동으로 기울기를 계산
# 영상의 히스토그램이 그레이스케일 전 구간에서 걸쳐 나타나도록 변경하는 선형 변환 기법

# 정규화 함수
# cv2.normalize(src, dst, alpha=None, beta=None, norm_type=None, dtype=None, mask=None) -> dst
# src : 입력 영상
# dst : 결과 영상 : python에서는 dst를 일반적으로 주지 않는다. None 주면 됨.
# alpha : (노름 정규화인 경우) 목표 노름 값,
#       : (원소 값 범위 정규화인 경우) 최소값
# bata : (원소 값 범위 정규화인 경우) 최대값
# norm_type : 정규화 타입. NORM_INF, NORM_L1, NORM_L2, NORM_MINMAX(MIN값과 MAX값을 원하는 값으로 한정).
# dtype : 결과 영상의 타입
# mask : 마스크 영상

# 히스토그램 스트레칭 변환 함수
# 변환 함수의 직선의 방정식 구하기
# 기울기 : 255 / (Gmax - Gmin)
# y 절편 : - 255 x Gmin / (Gmax - Gmin)
#   => g(x, y) = 255 / (Gmax - Gmin) x f(x, y) - 255 x Gmin / (Gmax - Gmin)
#              = (f(x, y) - Gmin) / (Gmax - Gmin) x 255


import sys
import numpy as np
import cv2


def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist


src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
# 수식으로 계산
gmin = np.min(src)
gmax = np.max(src)
dst = np.clip((src - gmin) * 255. / (gmax - gmin), 0, 255).astype(np.uint8)  # 실수 형태 이므로 255.


hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg2 = getGrayHistImage(hist2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)
cv2.imshow('histImg2', histImg2)
cv2.waitKey()

cv2.destroyAllWindows()

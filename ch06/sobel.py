# 영상의 미분과 소벨 필터

# 에지(edge)
# 영상에서 픽셀의 밝기 값이 급격하게 변하는 부분
# 일반적으로 배경과 객체, 또는 객체와 객체의 경계

# 에지 검출과 미분(변화율)
# 기본적인 에지 검출 방법
# 영상을 (x,y) 변수의 함수로 간주했을 때, 이 함수의 1차 미분(1st derivative)갑이 크게 나타나는 부분을 검출

# 1차 미분의 근사화(approximation) - 영상에서의 미분은 변화량의 최소 단위가 1픽셀 => h = 1
# 전진 차분(Forward difference) => (I(x+h) - I(x)) / h
# 후진 차분(Backward difference) => (I(x) - I(x-h)) / h
# 중앙 차분(Centered difference) => (I(x+h) - I(x-h)) / 2h ==> 중앙 차분 방법을 사용하는게 좀 더 정확하다.

# 소벨 필터를 이용항 미분 함수
# cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None) -> dst
# src : 입력 영싱
# ddepth : 출력 영상 데이터 타입. -1이면 입력 영상과 같은 데이터 타입을 사용.
# => 미분을 계산할 땐 그레이스케일은 좋지 않다. => 입력 영상이 그레이스케일이면 cv2.CV_32F로 float로 받는게 좋다.
# dx : x 방향 미분 차수.        # 대부분 dx=1, dy=0, ksize=3 또는
# dy : y 방향 미분 차수.        # dx=0, dy=1, ksize=3 으로 지정.
# dst : 출력 영상(행렬)
# ksize : 커널 크기. 기본값은 3
# scale : 연산 결과에 추가적으로 곱할 값. 기본값는 1.
# delta : 연산 결과에 추가적으로 더할 값. 기본값은 0.
# borderType : 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_DEFAULT

# 샤르 필터를 이용한 미분 함수 -> 많이 사용하진 않는다. 소벨 함수를 많이 씀.
# cv2.Scharr(src, ddepth, dx, dy, dst=None, scale=None, delta=None, borderType=None) -> dst


import sys
import numpy as np
import cv2

src = cv2.imread('ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

'''
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)

dx = cv2.filter2D(src, -1, kernel, delta=128)  # -1을 줘서 그레이스케일로 만들어지기 때문에 delta를 줘서 128을 더해준다.
'''

dx = cv2.Sobel(src, -1, 1, 0, delta=128)  # dx=1, dy=0 : x방향으로 미분하고 y방향으론 미분 X.
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()

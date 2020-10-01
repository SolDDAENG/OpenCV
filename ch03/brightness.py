# 영상의 밝기 조절

# 영상의 화소 처리 기법
# 화소 처리(Point processing)
# • 입력 영상의 특정 좌표 픽셀 값을 변경하여 출력 영상의 해당 좌표 픽셀 값으로 설정하는 연산
# dst(x, y) = f(src(x, y))  # f => 변환 함수(transfer function)  # src : source image(입력 이미지), dst : destination image(출력 이미지)
# • 결과 양상의 픽셀 값이 정해진 범위(e.g. 그레이스케일)에 있어야 함.
# • 반전, 밝기 조절, 명암비 조절 등

# 밝기 조절이란?
# • 영상을 전체적으로 더욱 밝거나 어둡게 만드는 연산.
# dst(x, y) = src(x, y) + n  ==> y = x + n 형태인 그래프.
# n은 양수일수도 있고 음수일수도 있다.
# saturate 연산 필요. ==> 255보다 크면 255, 0보다 작으면 0을 갖도록 한다.
# ==> dst(x, y) = saturate(src(x, y) + n)

# 영상의 밝기 조절을 위한 영상의 덧셈 연산. ==> add()함수를 사용하는것이 가장 좋다.
# cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst
# src1 : (입력) 첫 번째 영상 또는 스칼라
# src2 : (입력) 두 번쨰 영상 또는 스칼라
# dst : (출력) 덧셈 연산의 결과 영상
# mask : 마스크 영상
# dtype : 출력 영상(dst)의 타입. (e.g.)cv2.CV_8U, cv2_CV_32F 등
# 참고사항
# • 스칼라(Scalar)는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플
# • dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와 같아야 하며, 타입이 적절해야 함.


import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
# src = cv2.imread('ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('ch03/lenna.bmp')  # color로 이미지를 불러왔을땐 add()함수에서 B:100, G:0, R:0으로 적용된다.

if src is None:
    print('Image load failed!')
    sys.exit()

# dst = cv2.add(src, 100)  # == cv2.add(src, (100, 0, 0, 0))
dst = cv2.add(src, (100, 100, 100, 0))  # color image를 밝게 하기.
# dst = src + 100  # 100을 더해서 255보다 커지면 그 값을 0에 가까운 수로 바꾼다. (257이면 1로 저장됨.)
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)  # src + 100. => .을 찍어서 실수단위로 연산이 되게 해야한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

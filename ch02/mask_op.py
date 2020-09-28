# 마스크 연산과 ROI

# ROI : Region of Interest, 관심 영역
# 영상에서 특정 연산을 수행하고자 하는 임의의 부분 영역

# 마스크 연산
# OpenCV 는 일부 함수에 대해 ROI 연산을 지원하며 , 이때 마스크 영상 을 인자로 함께 전달해야 함
# (e.g.) cv2.copyTo(), cv2.calcHist(), cv2.bitwise_or(), cv2.matchTemplate(), etc.
# 마스크 영상은 cv2.CV_8UC1 타입 그레이스케일 영상
# 마스크 영상의 픽셀 값이 0 이 아닌 위치에서만 연산이 수행됨
# 보통 마스크 영상으로는 0 또는 255 로 구성된 이진 영상(binary image)을 사용

import sys
import cv2

# 마스크 영상을 이용한 영상 합성
src = cv2.imread('ch02/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('ch02/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('ch02/field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

# src, mask, dst는 모두 사이즈가 같아야 하고, src와 dst는 type이 같아야 한다.(src가 grayscale이면 dst도 grayscale), mask는 무조건 grayscale.
cv2.copyTo(src, mask, dst)
# dst[mask > 0] = src[mask > 0]  # 위와 같음. 메모리를 새롭게 만들어서 복사하는 것이 아닌 참조형태로 복사하는 것. ==> dst영상의 픽셀값 자체가 바뀐다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()


# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('ch02/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
# src영상에서 가로 세로는 그대로 가져오고 채널은 맨 마지막 채널 하나를 가지고 와서 마스크 영상으로 사용한다.
mask = src[:, :, -1]
# src는 src영상에서 가로 세로는 그대로 가져오고 채널은 0번째부터 3번째 까지 (0, 1, 2)의 채널을 가지고와서 src로 쓴다.
src = src[:, :, 0:3]
dst = cv2.imread('ch02/field.bmp', cv2.IMREAD_COLOR)

# cv2.copyTo(src, mask, dst)  # src, mask는 작은 크기릐 로고 영상이고 dst는 사이즈가 크기 때문에 그대로 사용하면 동작 X
# ==> 이것을 해결하기 위해 crop을 해야한다. (cropping : 그림의 원치 않는 바깥 부분을 제거하는 작업.)
h, w = src.shape[:2]

# crop = dst[0:h, 0:w]
crop = dst[100:h+100, 100:w+100]

cv2.copyTo(src, mask, crop)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()

cv2.destroyAllWindows()

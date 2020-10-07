# 리매핑(remapping)
# geometric transform을 전반적으로 일반화 시켜서 매핑하는 하나의 방법
# 영상의 특정 위치 픽셀을 다른 위치에 재배치하는 일반적인 프로세스
#   dst(x,y) = src(mapx(x,y), mapy(x,y))
# 어파인 변환, 투시 변환을 포함한 다양한 변환을 리매핑으로 표현 가능
# examples)
#   이동 변환                   대칭 변환
#   mapx(x,y) = x - 200       mapx(x,y) = w - 1 - x
#   mapy(x,y) = y - 100       mapy(x,y) = y

# cv2.remap(src, map1, map2, interpolation, dst=None, borderMode=None, borderValue=None) -> dst
# src : 입력 영상
# map1 : 결과 영상의 (x,y)좌표가 참조할 입력 영상의 x좌표.
#      : 입력 영상과 크기는 같고, 타입은 np.float32인 numpy.ndarray
# map2 : 결과 영상의 (x,y)좌표가 참조할 입력 영상의 y좌표.
# interpolation : 보간법
# dst : 출력 영상
# borderMode : 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
# borderValue : cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.


import sys
import numpy as np
import cv2


src = cv2.imread('ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

map2, map1 = np.indices((h, w), dtype=np.float32)  # np.indices() : 행렬의 인덱스값(x값과 y값)을 따로따로 행렬의 형태로 반환
map2 = map2 + 10 * np.sin(map1 / 32)  # sin함수처럼 파도가 있는 것처럼 출렁이게 만들기 위한 코드  # 10픽셀 만큼 출렁거리게 강조를 줬다.
# (map1 / 32) : map1 - x좌표 성분을 이용해서 파동이 만들어지게 함. 적당한값으로 나눠서 파동이 여러번 생기게 한다.
print(map1[0:5, 0:5])
print(map2[0:5, 0:5])

# dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)  # BORDER_DEFAULT : 영상 바깥에 가상의 픽셀이 있게 변환. 바깥쪽 근방의 픽셀이 대칭적으로 나타난다. -> 주변이 근방의 픽셀로 채워진다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

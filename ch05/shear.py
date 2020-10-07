# 영상의 전단 변환

# 전단 변환(Shear transformation)
# 층 밀림 변환. x축과 y축 방향에 대해 따로 정의.
# x' = x + my, y' = y
# x' = x, y' = mx + y

import sys
import numpy as np
import cv2


src = cv2.imread('ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# m = 0.5로 설정
aff = np.array([[1, 0.5, 0], [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
# dst = cv2.warpAffine(src, aff, (0, 0))
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))  # dsize는 정수형이어야 한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

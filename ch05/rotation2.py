# 영상의 회전

# 영상의 회전 변환 행렬 구하기 - 특정 좌표를 중심으로 회전할때의 어파인 변환 행렬
# cv2.getRotationMatrix2D(center, angle, scale) -> retval
# center : 회전 중심 좌표. (x,y)튜플
# angle : (반시계 방향) 회전 각도(degree). 음수는 시계 방향.
# scale : 추가적인 확대 비율
# retval : 2x3 어파인 변환 행렬. 실수형
#    α   β   (1-α) • center.x - β • center.y   where   α = scale • cos(angle)
#   -β   α   β • center.x + (1-α) • center.y           β = scale • sin(angle)

import sys
import numpy as np
import cv2


src = cv2.imread('ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)   # cp(center point)라고 하는 중심점의 좌표 계산
# rot = cv2.getRotationMatrix2D(cp, 20, 1)  # cp를 기준으로 반시계방향으로 20도 돌린다. 1 : 스케일링은 하지 않는다(영상의 크기 유지)
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

# dst = cv2.warpAffine(src, rot, (0, 0))
dst = cv2.warpAffine(src, rot, (0, 0), borderValue=(255, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

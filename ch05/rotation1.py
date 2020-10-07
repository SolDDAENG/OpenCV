# 영상의 회전

# 회전 변환(rotation transformation)
# 영상을 특정 각돤큼 회전시키는 변환(반시계 방향)
# x' = cosθ•x + sinθ•y
# y' = -sinθ•x + cosθ•y
# [x' = [[ cosθ  sinθ  0]     [x
#  y']   [-sinθ  cosθ  0 ]] *  y
#                              1]

import sys
import math
import numpy as np
import cv2


src = cv2.imread('ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

rad = 20 * math.pi / 180  # 20도를 radian 단위로 바꾼것.
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

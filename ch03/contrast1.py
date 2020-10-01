# 영상의 명암비 조절

# 명암비(Contrast)란?
# 밝은 곳과 어두운 곳 사이에 드러나는 밝기 정도의 차이
# 컨트라스트, 대비

# 기본적인 명암비 조절 함수
# dst(x, y) = saturate(s • src(x, y))  # 입력 영상에 scaling factor를 곱해서 결과 영상의 픽셀 값으로 셋팅
# => 단점 : s의 값에 따라 영상이 어두워지거나 전체적으로 포화되어 너무 밝아질 수 있다.

# 효과적인 명암비 조절 함수
# dst(X, y) = saturate(src(x, y) + (src(x, y) - 128) • α)
# (128, 128)을 무조건 지나고 기울기가 α의 값에 조절되는 직선의 방적식 그래프. (128은 고정이 아니고 영상에 따라 처리해줘야 한다.)
# src(x, y) + (src(x, y) - 128) • α ==> (1 + α) • src(x, y) - 128α


import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0  # contrast를 올릴 것이기 때문에 alpha값을 1.0으로 설정
dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)  # 0보다 작으면 0, 255보다 크면 255로 clipping

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

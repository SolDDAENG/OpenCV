# 샤프닝 : 언샤프 마스크 필터

# 언샤프 마스크(Unsharp mask) 필터링
# 날카롭지 않은(unsharp) 영상, 즉, 부드러워진 영상을 이용하여 날카로운 영상을 생성
# g(x) = f(x) - f'(x)
# h(x) = f(x) + g(x) = 2f(x) - f'(x)

# 언샤프 마스크 필터 구현하기
# - 샤프닝 정도를 조절할 수 있도록 수식 변경
# h(x,y) = f(x,y) + α⋅g(x,y)
#        = f(x,y) + α(f(x, y) - f'(x,y))
#        = (1+α)f(x,y) - α⋅f'(x,y)
# h(x,y) = (1+α)f(x, y) - α⋅Gσ(f(x,y))

import sys
import numpy as np
import cv2

src = cv2.imread('ch04/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)

# g(x) = f(x) - f'(x)
# dst = cv2.subtract(src, blr)
# dst = cv2.addWeighted(src, 1, blr, -1, 128)  # 결과를 잘 보이게 하기 위해서 128을 더해준다.
# dst = cv2.addWeighted(src, 2, blr, -1, 0)
dst = np.clip(2.0 * src - blr, 0, 255).astype(np.uint8)  # 내부 연산이 float형태로 계산되게끔 만들어 주는것이 좋다.


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

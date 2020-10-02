import sys
import numpy as np
import cv2

src = cv2.imread('ch04/rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

src_f = src_ycrcb[:, :, 0].astype(np.float32)  # x, y는 모두 가져오고 색상좌표 중에서 첫번째만(Y:밝기) 가져온다.
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)  # Y성분을 float형태로 컨버젼 후 사용. 
# => GaussianBlur()함수는 출력영상의 타입이 입력영상의 타입과 같게 설정된다. => blr로 실수 타입으로 출력된다.
# unit8타입으로 출력이 되면 GaussianBlur에 의해서 나타나는 출력영상의 소숫점 아래자리가 잘리게된다. => 미세한 변화가 사라지게 된다
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

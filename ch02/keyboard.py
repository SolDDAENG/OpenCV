# 키보드 이벤트 처리하기

# 키보드 입력 대기 함수
# cv2.waitKey(delay=None) -> retval
# delay : 밀리초 단위 대기 시간. delay <= 0 이면 무한히 기다림. 기본값은 0.
# retval : 입력된 키 값(ASCII code). 키가 입력되지 않으면 -1.

# 참고 사항
# - cv2.waitKey() 함수는 OpenCV 창이 하나라도 있을 때 동작함.
# - 특정 키 입력을 확인하려면 ord() 함수를 이용.
# while True:
#     if cv2.waitKey() == ord('q'):
#         break
# - 주요 특수키 코드 : 29(ESC), 13(ENTER), 9(TAB)
# 키보드 특수키 입력 처리하기
# - Windows 운영체제에서 방향키, 함수키 등의 특수키 입력은 cv2.waitKeyEx() 함수 사용

import sys
import numpy as np
import cv2

img = cv2.imread('ch02/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    key = cv2.waitKey()
    if key == 27:
        break

    elif key == ord('i') or key == ('I'):
        img = ~img
        cv2.imshow('image', img)

cv2.destroyAllWindows()

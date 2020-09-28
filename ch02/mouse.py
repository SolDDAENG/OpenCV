# 마우스 이벤트 처리하기

# 마우스 이벤트 콜백함수 등록 함수
# cv2.setMouseCallback(windowName, onMouse, param=None) -> None
# windowName : 마우스 이벤트 처리를 수행할 창 이름.
# onMouse : 마우스 이벤트 처리를 위한 콜백 함수 이름.
#         : 마우스 이벤트 콜백 함수는 다음 형식을 따라야 함.
#         : onMouse(event, x, y, flags, param) -> None
# param : 콜백 함수에 전달할 데이터

# 마우스 이벤트 처리 함수(콜백 함수) 형식
# onMouse(event, x, y, flags, param) -> None  # 꼭 onMouse 아니고 다른 이름으로 지정해도 된다.
# event : 마우스 이벤트 종류. cv2.EVENT_로 시작하는 상수.
# x, y : 마우스 이벤트 발생 좌표. (모니커 전체 화면에 대한 좌표가 아닌 내가 띄운 창에 대한 상대적인 좌표.)
# flags : 마우스 이벤트 발생 시 키보드 또는 마우스의 상태. cv2.EVENT_FLAG_로 시작하는 상수.
# param : cv2.setMouseCallback() 함수에서 설정한 데이터.

import sys
import numpy as np
import cv2

oldx = oldy = -1


def on_mouse(event, x, y, flags, param):  # param은 사용하지 않는 경우도 있지만 인자는 적어줘야 한다.
    global img, oldx, oldy  # img 변수를 함수 안에서 쓰기위해..

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN : {}, {}'.format(x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP : {}, {}'.format(x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # print('EVENT_MOUSEMOVE : {}, {}'.format(x, y))
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)  # 마우스를 빠르게 움직이면 그림이 끊기게 출력된다.
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5,
                     cv2.LINE_AA)  # circle()의 단점을 해결하기 위해 line() 사용
            cv2.imshow('image', img)
            oldx, oldy = x, y  # oldx, oldy를 업데이트 해서 선이 정상적으로 그려지게 한다.


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.imshow('image', img)

cv2.setMouseCallback('image', on_mouse)  # namedWindow() 또는 imshow() 함수가 호출된 이후에 호출해야 한다.

cv2.waitKey()

cv2.destroyAllWindows()

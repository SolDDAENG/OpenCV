# 트랙바 사용하기

# 트랙바(Trackbar)란?
# 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤
# OpenCV에서 제공하는 (유일한?) 그래픽 사용자 인터페이스

# 트랙바 생성 함수
# cv2.createTrackbar(trackbarName, windowName, value, count, onChange) -> None
# trackbarName : 트랙바 이름
# windowName : 트랙바를 생성할 창 이름.
# value : 트랙바 위치 초기값
# count : 트랙바 최대값. 최솟값은 항상 0.  # 최대값 위치가 트랙바에서 표현할 수 있는 단계의 갯수.
# onChange : 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름
#          : 트랙바 이벤트 콜백 함수는 다음 형식을 따름.
#          : onChange(pos) -> None

import numpy as np
import cv2


def on_level_changed(pos):
    global img

    # img => 0 ~ 255이기 때문에 16*16=256이 되면 255보다 크기 때문에 0으로 바뀐다. 이를 해결해주기 위한 코드를 작성해주어야 한다.
    level = pos * 16
    # if level >= 255:
    #     level = 255
    level = np.clip(level, 0, 255)  # level값의 최소를 0으로, 최대를 255로 고정 => 0보다 작으면 0, 255보다 크면 255.

    # img[:, :] = pos * 16  # pos가 0일땐 픽셀값이 0, 1일땐 16, 2일땐 32.... 
    img[:, :] = level
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)  # 트랙바도 창이 생성된 이후에 호출해야 한다.

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
# 카툰 필터 카메라
# 카메라 입력 영상에 실시간으로 재미있는 필터링을 적용하는 기능

# 구현 할 기능
# 카툰 필터
# 스케치 필터
# 스페이스바를 누를 때마다 모드 변경

# 카툰 필터 - 입력 영상의 색상을 단순화시키고, edge 부분을 검정색으로 강조
# 스케치 필터 - 평탄한 영역은 흰색. 에지 근방에서 어두운 영역을 검정색으로 설정.(밝은 영역은 흰색) - cv2.divide()


import sys
import numpy as np
import cv2


def cartoon_filter(img):
    h, w = img.shape[:2]
    img = cv2.resize(img, (w//2, h//2))  # 그냥 출력하면 영상이 느리기 때문에 줄이고 나중에 최종적으로 출력할떄 키운다. + 단순화 효과를 더 주기위해
    
    blr = cv2.bilateralFilter(img, -1, 20, 7)
    edge = 255 - cv2.Canny(img, 50, 120)  # 내부에서 자동으로 grayscale로 변환해준다.
    # 255 - cv2.Canny()해주지 않으면 edge부분은 흰색 나머지는 검정색으로 출력된다.
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)  # grayscale이기 때문에 blr와 and연산을 하기위해 color영상 형태로 변환해줘야 한다.
    
    dst = cv2.bitwise_and(blr, edge)  # and연산
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    # dst = cv2.resize(dst, (w, h))  # 위와 차이 비교해보기
    # interpolation=None(기본값)으로 쓰면 (블러된 느낌)자연스러운 값을 준다. => 카툰 필터를 할땐 값이 급격하게 바뀌는 느낌을 주기위해 cv2.INTER_NEAREST을 준다.

    return dst


def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(gray, blr, scale=255)  # gray를 blr로 나누고 255를 곱한다. 255를 곱해서 평탄한 영역은 흰색. 에지 근방에서 어두운 영역을 검정색으로 나타나도록 한다.
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)  # 입력 영상이 컬러 영상이기 때문에 dst도 컬러로 변환해주는게 나중에 좋을수도... 반드시 필요한 작업은 아님...
    
    return dst


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0


cap.release()
cv2.destroyAllWindows()

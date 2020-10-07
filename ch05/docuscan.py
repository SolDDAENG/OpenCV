# 문서 스캐너
# 카메라로 촬영한 문서 영사을 똑바로 펴서 저장해주는 프로그램

# 구현 할 기능
# 마우스로 문서 모서리 선택 & 이동하기
# 키보드 ENTER 키 인식
# 왜곡된 문서 영상을 직사각형 형태로 똑바로 펴기 (투시 변환)


import sys
import numpy as np
import cv2


def drawROI(img, corners):
    cpy = img.copy()

    c1 = (192, 192, 255)  # 1번 color  조금 더 밝은 핑크색
    c2 = (128, 128, 255)  # 2번 color  조금 더 어두은 핑크색

    for pt in corners:
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)

    cv2.line(cpy, tuple(corners[0]), tuple(corners[1]), c2, 2, cv2.LINE_AA)  # corners : ndarray로 되어있기 때문에 tuple로 변환해줘야 한다
    cv2.line(cpy, tuple(corners[1]), tuple(corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2]), tuple(corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3]), tuple(corners[0]), c2, 2, cv2.LINE_AA)

    # return cpy

    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)  # addWeighted()함수로 합성 -> 그림을 그린 부분에 배경도 살짝 보이게 함

    return disp

# 마우스 이벤트 처리
def onMouse(event, x, y, flags, param):  # onMouse()함수는 OpenCV에서 제공하는 콜백 함수 형식을 따라야 하기 때문에 5개의 파라미터를 꼭 가져야한다.
    # event : 마우스 이벤트
    # x, y : 좌표
    # flags : 마우스의 상태
    # param : setMouse콜백 함수에서 데이터를 보내오고 싶을때 사용
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i] - (x, y)) < 25:  # srcQuad의 모서리와 지금 클릭한 좌표의 거리가 25(circle의 반지름 25)보다 작을때
                dragSrc[i] = True
                ptOld = (x, y)  # 마우스를 드래그 할 때 원이 이동하는 변이를 알기 위해 ptOld 저장
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:  # dragSrc = True일때만
                dx = x - ptOld[0]  # 이전의 마우스 점에서 현재 얼만큼 이동했는지 계산
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy)  # 모서리 좌표 이동

                cpy = drawROI(src, srcQuad)  # 이동한만큼 결과를 화면에 출력
                cv2.imshow('img', cpy)
                ptOld = (x, y)  # ptOld를 현재 점으로 셋팅
                break


# 입력 이미지 불러오기
src = cv2.imread('ch05/scanned.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

# 입력 영상 크기 및 출력 영상 크기
h, w = src.shape[:2]
dw = 500  # 똑바로 편 이미지의 가로 크기 규정
dh = round(dw * 297 / 210)  # 세로 크기 계산  # A4 용지 크기: 210x297mm

# 모서리 점들의 좌표, 드래그 상태 여부
srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)  # 내가 선택하려고 하는 모서리 점 4개을 저장할 ndarray(초기 점의 좌표)
dstQuad = np.array([[0, 0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)  # 반시계방향으로 출력 영상의 4개의 모서리 위치
dragSrc = [False, False, False, False]  # 4개의 점 중에서 현재 어떤 점을 드래그하는지 상태 정보를 저장하기 위한 리스트  # 특정 점을 선택하면 해당 엘리먼트가 True로 잠깐 바뀐다.

# 모서리점, 사각형 그리기
disp = drawROI(src, srcQuad)

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER 키
        break
    elif key == 27:  # ESC 키
        cv2.destroyWindow('img')
        sys.exit()

# 투시 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)  # 3x3 투시 변환 행렬 리턴
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)  # (dw, dh) : 결과 영상 크기

# 결과 영상 출력
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

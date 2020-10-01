# 크로마 키(Chroma key) 합성
# 녹색 또는 파란색 배경에서 촬영한 영상에 다른 배경 영상을 합성하는 기술

# 구현할 기능
# 녹색 스크린 영역 추출하기
# 녹색 영역에 다른 배경 영상을 합성하여 저장하기
# 스페이스바를 이용하여 크로마 키 합성 동작 제어하기

# 녹색 스크린 영역 추출하기
# 크로마 키 영상을 HSV 색 공간으로 변환
# cv2.inRange() 함수를 사용하여사용하여 50 ≤ 𝐻 ≤ 80, 150 ≤ 𝑆 ≤ 255,0 ≤ 𝑉 ≤ 255 범위의 영역을 검출


import sys
import numpy as np
import cv2


# 녹색 배경 동영상
# cap1 = cv2.VideoCapture('woman.mp4')
cap1 = cv2.VideoCapture(0)

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비오는 배경 동영상
cap2 = cv2.VideoCapture('raining.mp4')  # 이 영상이 조금 더 짧다.

if not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print('w x h : {} x {}'.format(w, h))
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)  # 두개의 프레임 사이에 들어갈 시간 간격 계산

# 출력 동영상 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 합성 여부 플래그
do_composit = False  # 어떨 떄는 원본 영상을 보여주고 어떤 경우에는 합성 영상을 보여주기 위해 변수 정의
# True면 합성, False면 합성 X

# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()  # 첫 번째 동영상에서 한장의 영상을 받아온다.

    if not ret1:  # 맨 마지막 프레임까지 가면 여기서 걸린다.
        break
    
    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        ret2, frame2 = cap2.read()  # 두 번째 동영상에서 한장의 영상을 받아온다.

        if not ret2:
            break

        frame2 = cv2.resize(frame2, (w, h))  # 카메라를 킬 경우 카메라의 사이즈가 달라 에러가 발생한다. => resize해주기

        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        mask = cv2.inRange(hsv, (50, 70, 0), (70, 255, 255))  # 뒷 배경에 따라 색 범위 조정하기
        cv2.copyTo(frame2, mask, frame1)  # frame2애서 mask가 흰색인 부분만 frame1으로 복사  # 카메라를 킬 경우 카메라의 사이즈가 달라 에러가 발생한다. => resize해주기

    out.write(frame1)  # 출력 영상에 저장

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 do_composit 플래그를 변경
    if key == ord(' '):  # 스페이스바를 누르면 do_composit이 True, False 변환
        do_composit = not do_composit
    elif key == 27:  # ESC누르면 while루프 종료.
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

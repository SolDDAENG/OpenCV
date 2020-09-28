# 실전 코딩 : 동영상 전환 이펙트

# 동영상 전환 이펙트
# - 두 동영상 클립 사이에 추가되는 애니메이션 효과
# - 페이드-인(fade-in), 페이드-아웃(fade-out), 디졸브(dissolve), 밀기, 확대 등

# 구현 할 기능
# 두 개의 동영상 동시 열기
# 첫 번째 동영상의 마지막 N개 프레임과 두 번째 동영상의 처음 N개 프레임 합성
# 합성된 영상을 동영상으로 저장하기

import sys
import numpy as np
import cv2

# 두 개의 동영상 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('ch02/video1.mp4')
cap2 = cv2.VideoCapture('ch02/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video load failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함.
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))  # 1번 동영상의 전체 프레임 수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))  # 2번 동영상의 전체 프레임 수
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)  # 첫 번째 동영상의 끝부분 2초, 두 번째 동영상의 2초가 겹쳐져서 합성이 되게끔 하기위해...

print('frame_cnt1 : ', frame_cnt1)
print('frame_cnt2 : ', frame_cnt2)
print('FPS : ', fps)

delay = int(1000 / fps)  # 두 프레임 사이의 시간 간격을 계산한 수식

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('ch02/output2.avi', fourcc, fps, (w, h))  # 동영상을 저장하는 코드

# 1번 동영상 복사
for i in range(frame_cnt1 - effect_frames):  # 첫번째 동영상
    ret1, frame1 = cap1.read()

    if not ret1:  # 동영상의 마지막 프레임이 되면 break
        break

    out.write(frame1)  # frame1에서 effect_frames을 뺀 나머지 저장
    print('.', end='')

    cv2.imshow('frame', frame1)
    # cv2.waitKey(delay)
    cv2.waitKey(1)

# 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()

    # 합성
    dx = int(w * i / effect_frames)

    # 밀어내기 효과
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx] = frame2[:, 0:dx]
    frame[:, dx:w] = frame1[:, dx:w]

    # 디졸브 효과
    # alpha = 1.0 - i / effect_frames  # alpha는 0 ~ 1 사이의 값으로 만들어야 한다.  # i = 0이면 alpha = 1
    # frame = cv2.addWeighted(frame1, alpha, frame2, 1 - alpha, 0)  # addWeighted() : 가중치 합 구하기 함수.

    out.write(frame)
    print('.', end='')

    cv2.imshow('frame', frame)
    # cv2.waitKey(delay)
    cv2.waitKey(1)

# 2번 동영상 복사
for i in range(effect_frames, frame_cnt2):  # 두번째 동영상  # effect_frames부터 시작해서 frame_cnt2 마지막 프레임까지
    ret2, frame2 = cap2.read()

    if not ret2:  # 동영상의 마지막 프레임이 되면 break.
        break

    out.write(frame2)
    print('.', end='')

    cv2.imshow('frame', frame2)
    cv2.waitKey(delay)

print('\noutput.avi file is successfully generated!')

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
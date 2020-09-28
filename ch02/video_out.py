# 카메라와 동영상 처리하기 2

# cv2.VideoWriter 클래스
# - OpenCV에서는 cv2.VideoWriter 클래스를 이용하여 일련의 프레임을 동영상 파일로 저장할 수 있음.
# - 일련의 프레임은 모두 크기와 데이터 타입이 같아야 함.

# Fourcc (4-문자 코드, four character code)
# - 동영상 파일의 코덱, 압축 방식, 색상, 픽셀 포맷 등을 정의하는 정수 값.
# cv2.VideoWriter_fourcc(*'DIVX') : DIVX MPED-4 코덱
# cv2.VideoWriter_fourcc(*'XVID') : XVID MPED-4 코덱
# cv2.VideoWriter_fourcc(*'FMP4') : FFMPEG MPED-4 코덱
# cv2.VideoWriter_fourcc(*'X264') : H.264/AVC 코덱
# cv2.VideoWriter_fourcc(*'MJPG') : Motion-JPEG 코덱

import sys
import cv2

# 웹카메라 입력을 동영상으로 저장하기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# get함수는 float값을 리턴하기 때문에 정수로 변환하기 위해서 round함수를 사용했다.
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
fps = 30

# *'DIVX' == 'D', 'I', 'V', 'X' 이렇게 써도 된다. * : 문자열을 풀어서 쓰는 개념
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)  # 한 프레임과 그 다음 프레임 사이의 시간 간격 계산

out = cv2.VideoWriter('ch02/output.avi', fourcc, fps, (w, h)
                      )  # VideoWriter라는 클래스 객체를 만드는 코드

if not out.isOpened():
    print('File open failed!')
    cap.release()  # 저장이 안되면 카메라도 닫고
    sys.exit()     # 프로그램 종료

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # inversed = ~frame  # 프레임 반전
    edge = cv2.Canny(frame, 50, 150)  # edge는 grayscale 형태이고 VideoWriter는 color영상으로 만들었기 때문에 저장되지 않는다.   
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)  # 이를 해결하기 위해 cvtColor 함수를 이용해 BGR값이 있게 변환해준다.

    # OpenCV에서 제공하는 VideoWriter는 영상데이터만 저장하고 소리는 저장X
    # out.write(inversed)
    # out.write(frame)
    out.write(edge_color)

    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)
    cv2.imshow('edge_color', edge_color)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

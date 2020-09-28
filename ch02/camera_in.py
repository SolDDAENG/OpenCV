# 카메라와 동영상 처리하기 1

# 카메라 열기
# cv2.VideoCapture(index, apiPreference=None) -> retval
# index : camera_id + domain_offset_id. 시스템 기본 카메라를 기본 방법으로 열려면 index에 0을 전달
# apiPreference : 선호하는 카메라 처리 방법을 지정.
# retval : cv2.VideoCapture 객체

# 동영상 열기
# cv2.VideoCapture(filename, apiPreference=None) -> retval
# filename : 비디오 파일 이름, 정지 영상 시퀀스, 비디오 스트림 URL등. (e.g.) 'video.avi', 'img_%02d.jpg', 'protocol://host:port/script?params|auth'

# cv2.VideoCapture.open(index, apiPreference=None) -> retval
# retval : 성공하면 True, 실패하면 False.
# 카메라를 열땐 index에 숫자가 들어가고, 동영상을 열땐 index 자리에 동영상 파일의 이름이 들어간다.

# 비디오 캡쳐가 준비되었는지 확인
# cv2.VideoCapture.isOpened() -> retval

# 프레임 받아오기
# cv2.VideoCapture.read(image=None) -> retval, image
# retval : 성공하면 True, 실패하면 False.
# image : 현재 프레임 (numpy.ndarray)


import sys
import cv2

cap = cv2.VideoCapture(0)  # 카메라.  # ()안에 0을 넣으면 open()함수를 안써도 된다.
# cap.open(0)
# cap = cv2.VideoCapture('ch02/video1.mp4')  # 동영상

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 카메라 프레임의 속성을 받아올 수 있다.
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

print(w, h)

while True:
    ret, frame = cap.read()  # 현재 오픈되어 있는 카메라에서 한 프레임씩 받아온다.
    # frame만 쓰면 True, False만 저장이 되기 때문에 ret도 같이 써줘야 한다.
    # ret, frame 순서도 기억하기.

    if not ret:  # 동영상의 경우 동영상의 마지막 프레임까지 가게되면 여기 if문에 자동으로 걸린다. ==> 동영상이 종료된다.
        break

    # while 루프 안에서 frame이라는 정지 영상을 처리하는 코드를 작성할 수 있다.
    edge = cv2.Canny(frame, 30, 150)  # 윤곽선이 저장된 edge라고 하는 영상을 만든다.
    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('inversed', inversed)
    if cv2.waitKey(20) == 27:  # 20m/s 기다렸다가 다음 프레임을 받아온다.  # ESC를 누르면 종료(27:ESC)
        break

cap.release()  # 오픈한 캡쳐 객체를 해제.
cv2.destroyAllWindows()

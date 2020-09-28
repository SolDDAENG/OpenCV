# OpenCV 그리기 함수

import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)  # 400 x 400의 컬러 이미지를 만든다. 초기값을 255으로 줬기 때문에 전체 BGR값이 모두 255로 셋팅되므로 흰색이다.

# cv2.line() : 직선 그리기 함수.
# cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img
# lineType : 선 타입. cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA 중 선택. 기본값은 cv2.LINE_8
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# 사각형 그리기
# cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img)
# pt1, pt2 : 사각형의 두 꼭지점 좌표. (x1,y1)튜플
# rec : 사각형 위치 정보. (x,y,w,h) 튜플
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)  # rec
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)  # pt1, pt2

# 원 그리기
# cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None) -> img
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)  # 원, 타원, 문자를 출력할땐 cv2.LINE_AA를 주는 것이 확대했을 때 더 부드럽다.
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형 그리기
# cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None) -> img
# pts : 다각형 외곽 점들의 좌표 배열(꼭지점 좌표). numpy.ndarray의 리스트. (e.g.) [np.array([[10, 10], [50, 50], [10, 50]], dtype=np.int32)]
# isClosed : 폐곡선 여부. True 또는 False 지정.
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)  # [pts]로 리스트 형태로 감싸서 입력해줘야 한다.

# 문자열 출력
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None) -> img
# org : 영상에서 문자열을 출력할 위치의 좌측 하단 좌표
# fontFace : 폰트 종류. cv2.FONT_HERSHEY_로 시작하는 상수 중 선택
# fontScale : 폰트 크기 확대/축소 비율
# thickness : 선 두께. 기본값은 1. 음수(-1)를 지정하면 내부를 채움.
# bottomLeftOrigin : True이면 영상의 좌측 하단을 원점으로 간주. 기본값은 False.
text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

# 연산 시간 측정 방법

# 컴퓨터 비전은 대용량 데이터를 다루고, 일련의 과정을 통해 최종 결과를 얻으므로 매 단계에서 연산 시간을 측정하여 관리할 필요가 있다.

# OpenCV에서는 TickMeter 클래스를 이용하여 연산 시간을 측정
# cv2.TickMeter() -> tm
# tm : cv2.TickMeter 객체
# tm.start() : 시간 측정 시작
# tm.stop() : 시간 측정 끝
# tm.reset() : 시간 측정 초기화

# tm.getTimeSec() : 측정 시간을 초 단위로 반환
# tm.getTimeMilli() : 측정 시간을 밀리 초 단위로 반환
# tm.getTimeMicro() : 측정 시간을 마이크로 초 단위로 반환


import sys
import time
import numpy as np
import cv2

img = cv2.imread('ch02/hongkong.jpg')

if img is None:
    print('Image load failed!')
    sys.exit()

tm = cv2.TickMeter()

tm.reset()
tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)  # tm.start()와 tm.stop() 안에 넣어줘야 한다.

tm.stop()
ms = tm.getTimeMilli()

print('time : ', (time.time() - t1) * 1000)
print('Elapsed time : {}ms'.format(ms))
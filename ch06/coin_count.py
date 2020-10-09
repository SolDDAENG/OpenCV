# 동전 카운터
# 영상의 동전을 검출하여 얼마인지를 자동으로 계산하는 프로그램
# 편의상 동전은 100원짜리와 10원짜리만 있다고 가정

# 구현할 기능
# 동전 검출하기 -> 허프 원 검출
# 동전 구분하기 -> 색상 정보 이용

# 동전 검출하기
# 동그란 객체는 동전만 있다고 가정
# -> cv2.HoughCircles() 함수 사용
# 영상 크기 : 800x600(px)
# 동전 크기 : 100원: 약 100x100(px). 10원: 약 80x80(px)

# 동준 구분하기
# 동전 영역 부분 영상 추출 -> HSV 색 공간으로 변환
# 동전 영역에 대해서만 Hue 색 성분 분포 분석
# 동전 영역 픽셀에 대해 Hue 값을 +40만큼 시프트하고, Hue 평균을 분석  # 180보다 커지면 다시 0으로
#   - Hue 평균이 90보다 작으면 10원
#   - Hue 평균이 90보다 크면 100원


import sys
import numpy as np
import cv2


# 입력 이미지 불러오기
# src = cv2.imread('ch06/coins1.jpg')
src = cv2.imread('ch06/coins2.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1)

# 허프 변환 원 검출
circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                           param1=150, param2=40, minRadius=20, maxRadius=80)

# 원 검출 결과 및 동전 금액 출력
sum_of_money = 0  # 동전의 금액을 저장할 변수
dst = src.copy()
if circles is not None:
    for i in range(circles.shape[1]):  # circles.shape[1] : 원의 갯수
        cx, cy, radius = circles[0][i]  # cx, cy, radius는 double형태의 실수 -> int로 변환해줘야 한다.
        radius = int(radius)
        cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

        # 동전 영역 부분 영상 추출
        x1 = int(cx - radius)  # cx, cy, radius는 double형태의 실수 -> 정수형 형탸의 int로 변환
        y1 = int(cy - radius)
        x2 = int(cx + radius)
        y2 = int(cy + radius)
        radius = int(radius)
        
        crop = dst[y1:y2, x1:x2, :]
        # crop = src[y1:y2, x1:x2, :]
        ch, cw = crop.shape[:2]

        # 동전 영역에 대한 ROI 마스크 영상 생성 - 배경(마루 바닥)의 영상을 제거
        mask = np.zeros((ch, cw), np.uint8)  # 배경(마루 바닥)의 영상을 제거하기 위해 mask를 만든다.
        cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)
        # mask도 같이 입력으로 주고 mask영상의 흰색 부분만 Hue값 계산

        # 동전 영역 Hue 색 성분을 +40 시프트하고, Hue 평균을 계산
        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        hue, _, _ = cv2.split(hsv)
        hue_shift = (hue + 40) % 180  # 180보다 커지면 다시 0으로 가게 하기위해 나눗셈 나머지 연산
        mean_of_hue = cv2.mean(hue_shift, mask)[0]  # mask를 인자로 줘서 원 안에 있는것만 계산  # mean() 결과는 4개짜리 더블 값으로 나오는데 그중 첫번째만 사용

        print(mean_of_hue)

        # cv2.imshow('crop', crop)
        # cv2.imshow('mask', mask)
        # cv2.waitKey()

        # Hue 평균이 90보다 작으면 10원, 90보다 크면 100원으로 간주
        won = 100
        if mean_of_hue < 90:
            won = 10

        sum_of_money += won

        cv2.putText(crop, str(won), (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (255, 0, 0), 2, cv2.LINE_AA)

cv2.putText(dst, str(sum_of_money) + ' won', (40, 80),
            cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

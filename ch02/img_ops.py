# 영상의 생성, 복사, 부분 영상 추출

import numpy as np
import cv2

# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)  # grayscale image
img2 = np.zeros((240, 320, 3), dtype=np.uint8)  # color image
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow
# np.full() : 모든 값을 지정하는 숫자로 채운다.

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('ch02/HappyFish.jpg')
# img2 = img1
# img3 = img1.copy()
img2 = img1[40:120, 30:150]
img3 = img1[30:120, 30:150].copy()

# img1[:, :] = (0, 255, 255)  # img1, img2는 노란색으로 나오고 img3는 변하기 전 img1이 나온다.

# img1.fill(255)
# img2.fill(0)  # img2 뿐만 아니라 img1도 바뀐다.
cv2.circle(img2, (50, 50), 20, (0, 0, 255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('ch02/HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

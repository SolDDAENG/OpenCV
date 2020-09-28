# 영상의 속성과 픽셀 값 참조

import sys
import cv2

# 영상 불러오기
img1 = cv2.imread('ch02/cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('ch02/cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print('type(img1) : ', type(img1))
print('img1.shape : ', img1.shape)
print('img2.shape : ', img2.shape)
print('img1.dtype : ', img1.dtype)
print('img2.dtype : ', img2.dtype)

# 영상의 크기 참조
h, w = img1.shape
print('img1 size : {} x {}'.format(w, h))

h, w = img2.shape[:2]  # color이기 때문에 2번째 값 까지만 주어야 한다.
print('img2 size : {} x {}'.format(w, h))

# if img1.ndim == 2:
if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
'''
for y in range(h):  # 실제로 이 방법은 너무 느려서 하면 안된대요. ==> 가급적이면 opencv나 numpy에서 제공하는 방법을 이용하기.
    for x in range(w):  # x가 0부터 w-1까지 증가
        img1[y, x] = 255
        img2[y, x] = (0, 255, 255)
'''

img1[:, :] = 0
img2[:, :] = (0, 255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()

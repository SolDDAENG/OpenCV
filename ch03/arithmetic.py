# 영상의 산술 및 논리 연산
# 덧셈 연산
# dst(x, y) = saturate(src1(x, y) + src2(x, y))
# 두 영상의 같은 위치에 존재하는 픽셀 값을 더하여 결과 영상의 픽셀 값으로 설정
# 덧셈 결과가 255보다 크면 픽셀 값을 255로 설정 (포화 연산)

# 덧셈 연산
# cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst
# src1 : (입력) 첫 번째 영상 또는 스칼라
# src2 : (입력) 두 번쨰 영상 또는 스칼라
# dst : (출력) 덧셈 연산의 결과 영상 ==> dst를 인자로 줄 수도 있고 출력으로 받을 수도 있지만 결과 형태로 받는 것이 일반적이다.
# mask : 마스크 영상 ==> 영상 전체가 아닌 일부 영역에만 덧셈 연산(add()함수)를 수행 할 수 있다. ==> 픽셀값이 0이 아닌 부분에서면 덧셈 연산이 이루어진다.
# dtype : 출력 영상(dst)의 타입. (e.g.)cv2.CV_8U, cv2_CV_32F 등. ==> src1과 src2의 타입이 다른 경우 지정해줘야한다. numpy의 dtype이 아닌 cv2의 dtype(flag형식 : cv2.CV_8U, cv2_CV_32F)
# 참고사항
# • 스칼라(Scalar)는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플
# • dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와 같아야 하며, 타입이 적절해야 함.

# 가중치 합(weighted sum)
# dst(x, y) = saturate(α • (src1(x, y) + β • src2(x, y))
# α, β : weight. α + β 이 1보다 크면 위의 연산이 255보다 커지므로 전체적으로 밝아지는 영상이 만들어지게 된다.
# • 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 가중합을 계산하여 결과 영상의 픽셀 값으로 설정
# • 보통 α + β = 1 이 되도록 설정 => 두 입력 영상의 평균 밝기를 유기

# cv2.addWeighted(src1, alpha, scr2, beta, gamma, dst=None, dtype=None) -> dst
# src1 : 첫 번째 영상
# alpha : 첫 번째 영상 가중치
# src2 : 두 번째 영상. src1과 같은 크기 & 같은 타입
# beta : 두 번째 영상 가중치
# gamma : 결과 영상에 추가적으로 더할 값. 더할 값이 없으면 0 주면 된다.
# dst : 가중치 합 결과 영상 => 함수의 반환값으로 받는 경우가 일반적이다.
# dtype : 출력 영상(dst)의 타입

# 평균 연산(average)
# • 가중치를 α = β = 0.5 로 설정한 가중치 합
# dst(x, y) = 1/2(src1(x, y) + src2(x, y))

# 뺄셈 연산
# dst(x, y) = saturate(src1(x, y) - src2(x, y))
# • 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺄셈 연산을 수행하여 결과 영상의 픽셀 값으로 설정. => 뺄셈의 순서에 따라 결과값이 달라지므로 순서가 중요.
# • 뺄셈 결과가 0보다 작으면 픽셀 값을 0으로 설정 (포화 연산)

# cv2.subtract(src1, src2, dst=None, mask=None, dtype=None) -> dst
# src1 : 첫 번째 영상 또는 스칼라
# src2 : 두 번째 영상 또는 스칼라
# dst : 뺄셈 연산 결과 영상
# mask : 마스크 영상
# dtype : 출력 영상(dst)의 타입

# 차이 연산 => 변화가 있는 부분을 찾고자 할 때 사용한다.
# dst(x, y) = |src1(x, y) - src2(x, y)|
# • 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺄셈 연산을 수행한 후, 그 절대값을 결과 영상의 픽셀값으로 설정
# • 뺄셈 연산과 달리 입력 영상의 순서에 영향을 받지 않음.
# cv2.absdiff(src1, src2, dst=None) -> dst
# src1 : 첫 번째 영상 또는 스칼라
# src2 : 두 번째 영상 또는 스칼라
# dst : 차이 연산 결과 영상(차영상)

# 영상의 논리 연산
# 비트단위 AND, OR, XOR, NOT 연산
# cv2.bitwise_and(src1, src2, dst=None, mask=None) -> dst
# cv2.bitwise_or(src1, src2, dst=None, mask=None) -> dst
# cv2.bitwise_xor(src1, src2, dst=None, mask=None) -> dst
# cv2.bitwise_not(src1, src2, dst=None, mask=None) -> dst
# src1 : 첫 번째 영상 또는 스칼라
# src2 : 두 번쨰 영상 또는 스칼라
# dst : 출력 영상
# mask : 마스크 영상
# 참고사항 : 각각의 픽셀 값을 이진수로 표현하고, 비트(bit)단위 논리 연산을 수행


import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('ch03/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch03/square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)  # 0.5, 0.5의 가중치를 줬다 ==> 평균을 계산
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()

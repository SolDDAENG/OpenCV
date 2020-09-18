import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('ch01/cat.bmp')
# imread() 함수로 불러온 영상의 색상 정보는 BGR 순서이므로 matplotlib으로 불러오기 위해선 RGB 순서도 변경해줘야 한다.
# ==> cv2.cvtColor() 함수 이용
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')  # off안하면 영상 좌표축이 생긴다.
plt.imshow(imgRGB)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.show()

# 그레이 스케일 영상 출력
imgGray = cv2.imread('ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')  # graysacle 영상을 출력하려면 cmap='gray'(cmap : color map)을 지정해줘야 한다.
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
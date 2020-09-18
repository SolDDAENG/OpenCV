import sys
import cv2


print('Hello OpenCV', cv2.__version__)

# img = cv2.imread('ch01/cat.bmp', cv2.IMREAD_COLOR)  # BGR 컬러 영상으로 읽기 (기본값)  # shape = (rows, cols, 3)
# 그레이 스케일 영상으로 읽기  # shape = (rows, cols)
img = cv2.imread('ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('ch01/cat.bmp', cv2.IMREAD_UNCHANGED)  # 영상 파일 속성 그대로 읽기  # (e.g.) 투명한 PNG 파일  # shape = (rows, cols, 4)  # 4 ==> BGR + 1(alpha : 투명한 채널)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imwrite('ch01/caht_gray.png', img)

cv2.namedWindow('image')
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# WINDOW_NORMAL : 영상 크기를 창 크기에 맞게 지정 ==> 영상이 너무 큰 경우에만 사용하는 것이 좋다.
# WINDOW_AUTOSIZE : 창 크기를 영상 크기에 맞게 변경 (기본값)

# cv2.namedWindow('image')를 생략해도 imshow가 image라는 이름으로 창을 만든다. ==> 영상의 크기가 너무 크지 않다면 namedWindow 생략해서 써도 된다.
cv2.imshow('image', img)

# key = cv2.waitKey(2000)  # waitKey가 없으면 창이 생성되지 않는다.
# print(key)
while True:
    # if cv2.waitKey() == 27:  # 27(ESC), 13(ENTER), 9(TAB)
    if cv2.waitKey() == ord('q'):
        break

# cv2.destroyAllWindows()
cv2.destroyWindow('image')

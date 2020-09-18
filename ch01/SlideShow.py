import sys
import glob
import cv2

# 이미지 파일을 모두 img_files 리스트에 추가
img_files = glob.glob('ch01/images/*.jpg')

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

# 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 전체 화면으로 실행하려면 WINDOW_NORMAL로 해야한다.
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 무한 루프
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:  # 키보드 아무것도 눌리지 않으면 -1, 아무거나 눌러도 0보다 크다.
        break

    idx += 1
    if idx >= cnt:  # idx가 cnt보다 같거나 커지면 다시 처음 영상을 보여준다.
        idx = 0

cv2.destroyAllWindows()
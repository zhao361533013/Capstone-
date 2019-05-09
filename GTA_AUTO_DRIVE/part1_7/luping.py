from PIL import ImageGrab
import numpy as np
import cv2
import time

for i in list(range(4))[::-1]:
    print(i + 1)
    time.sleep(1)
screen = ImageGrab.grab()  # 获得当前屏幕

length, width = screen.size  # 获得当前屏幕的大小
video_decode_style = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
video = cv2.VideoWriter('b.avi', video_decode_style, 32, (length, width))  # 输出文件命名为a.mp4,帧率为32，可以调节
while True:
    im = ImageGrab.grab()
    imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR格式
    video.write(imm)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('stop')
        break
video.release()
cv2.destroyAllWindows()

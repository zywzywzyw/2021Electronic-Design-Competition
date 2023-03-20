#最终巡线部分代码

import sensor, image, time

sensor.reset(freq=30000000)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(False)  # 必须关闭此功能，以防止图像冲洗…
sensor.set_auto_whitebal(False)  # 必须关闭此功能，以防止图像冲洗…
sensor.skip_frames(time = 2000)

from fpioa_manager import fm

# need your connect hardware IO 9/10 to loopback
fm.register(9, fm.fpioa.UART1_TX, force=True)
fm.register(10, fm.fpioa.UART1_RX, force=True)
from machine import UART

uart_A = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)


red_threshold   = (0,100,0,255,-255,255)
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs_b = img.find_blobs([red_threshold],roi=(210,0,80,240),area_threshold=500,merge=True)
    if blobs_b:
        for b in blobs_b:
            tmp=img.draw_rectangle(b[0:4],color=(0,255,0))
            tmp=img.draw_cross(b[5], b[6])
            print(b.rotation()*360/3.14)
            print(b.cy())
            if  b.area()<15000:
                if b.cy() > 110 :
                    uart_A.write("3")
                elif b.cy() < 90:
                    uart_A.write("1")
                else:uart_A.write("2")
            else:
                uart_A.write("c")
                print("sbakjbkjsdbkjfbsjdkf")
                #while 1:pass
            #if b.rotation()*360/3.14 >5 and b.rotation()*360/3.14 >0:
    print(clock.fps())


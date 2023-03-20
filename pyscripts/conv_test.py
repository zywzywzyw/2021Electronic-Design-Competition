# Untitled - By: lenovo - 周五 10月 29 2021

import sensor, image, time,lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQQVGA)
sensor.skip_frames(time = 2000)
conv_a=(0,1/3,0,0,1/3,0,0,1/3,0)
conv_b=(1/6,1/6,1/6,-1/3,-1/3,-1/3,1/6,1/6,1/6)
lcd.init()
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    #lcd.display(img)
    #img.conv3(conv_a)
    img.conv3(conv_b)
    lcd.display(img)

    print(clock.fps())

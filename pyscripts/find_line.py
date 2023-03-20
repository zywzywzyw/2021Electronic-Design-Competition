#使用find_line进行巡线，帧率低且无法有效识别岔路
THRESHOLD = (0, 80) # Grayscale threshold for dark things...

#设置是否使用img.binary()函数进行图像分割
BINARY_VISIBLE = True # 首先执行二进制操作，以便您可以看到正在运行的线性回归...虽然可能会降低FPS。

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot().binary([THRESHOLD]) if BINARY_VISIBLE else sensor.snapshot()

    # 函数返回回归后的线段对象line，有x1(), y1(), x2(), y2(), length(), theta(), rho(), magnitude()参数。
    # x1 y1 x2 y2分别代表线段的两个顶点坐标，length是线段长度，theta是线段的角度。
    # magnitude表示线性回归的效果，它是（0，+∞）范围内的一个数字，其中0代表一个圆。如果场景线性回归的越好，这个值越大。
    line = img.get_regression([(255,255) if BINARY_VISIBLE else THRESHOLD],roi=(0,0,20,60),robust = True)

    if (line): img.draw_line(line.line(), color = 127)
    print("FPS %f, mag = %s" % (clock.fps(), str(line.magnitude()) if (line) else "N/A"))
    print(line.theta() if(line) else "N/A")
    if line :
        if line.theta()>30 and line.theta()<60:
            print("RRRRRRRRRRRRRRRRRRRR")
    line1=line
    line = img.get_regression([(255,255) if BINARY_VISIBLE else THRESHOLD],roi=(60,0,20,60),robust = True)

    if (line): img.draw_line(line.line(), color = 127)
    print("FPS %f, mag = %s" % (clock.fps(), str(line.magnitude()) if (line) else "N/A"))
    print(line.theta() if(line) else "N/A")
    if line :
        if line.theta()>120 and line.theta()<150:
            print("LLLLLLLLLLLLLLLLLLLLL")
    line2=line
    line = img.get_regression([(255,255) if BINARY_VISIBLE else THRESHOLD],robust = True)

    if (line): img.draw_line(line.line(), color = 127)
    print("FPS %f, mag = %s" % (clock.fps(), str(line.magnitude()) if (line) else "N/A"))
    print(line.theta() if(line) else "N/A")
    if line :
        if line.theta()>150 or line.theta()<30:
            print("111111111111111111111")

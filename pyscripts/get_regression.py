#通过回归进行巡线 耗时久，效果差
THRESHOLD = (0, 40) # Grayscale threshold for dark things...
import sensor, image, time

sensor.reset()
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQQVGA) # 80x60 (4,800 pixels) - O(N^2) max = 2,3040,000.
#sensor.set_windowing([0,20,80,40])
sensor.skip_frames(time = 2000)     # WARNING: If you use QQVGA it may take seconds
clock = time.clock()                # to process a frame sometimes.


def draw_l(l):
    if (line):
        print(line.theta())
        rho_err = abs(line.rho())-img.width()/2
        if line.theta()>90:
            theta_err = line.theta()-180
        else:
            theta_err = line.theta()
        if line.magnitude()>5:
            img.draw_line(line.line(), color = 255)
            print(rho_err,line.magnitude())
        else:
            pass
    else:
        pass
while(True):
    clock.tick()
    img = sensor.snapshot().binary([THRESHOLD])
    """
    line = img.get_regression([(100,100)], robust = True,roi=(0,0,26,30))
    draw_l(line)
    line = img.get_regression([(100,100)], robust = True,roi=(26,0,26,60))
    draw_l(line)
    line = img.get_regression([(100,100)], robust = True,roi=(52,0,26,30))
    draw_l(line)
    """
    line = img.get_regression([(100,100)], robust = True)
    draw_l(line)
    print(clock.fps())

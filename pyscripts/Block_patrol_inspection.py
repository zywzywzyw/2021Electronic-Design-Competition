import sensor
import image
import lcd
import time

def draw_avg(a):
    sumx,sumy=0,0
    for b in a:
        sumx=b[5]+sumx
        sumy=b[6]+sumy
        tmp=img.draw_rectangle(b[0:4])
        tmp=img.draw_cross(b[5], b[6])
        c=img.get_pixel(b[5], b[6])
        #print(b)
    if a:
        sumx=sumx/len(a)
        sumy=sumy/len(a)
        #print(sumx,sumy)
    return [sumx,sumy]

def draw_divd(a):
    for b in a:
        tmp=img.draw_rectangle(b[0:4])
        tmp=img.draw_cross(b[5], b[6])
        c=img.get_pixel(b[5], b[6])
        print(b)
    if a:
        if len(a) > 1 or a[0][4] > 8000 :
            print('y')

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
thresholds   = (10,30,20,30,10,20)
p_threshold=1
b1,b2=[0,0]
blobs_1,blobs_2,blobs_3,blobs_4=[0,0,0,0]
#x=(-2,-2,0,-2,0,2,0,2,2)
while True:

    img=sensor.snapshot()
    #img.conv3(x)
    blobs_1 = img.find_blobs([thresholds],x_stride=1, y_stride=1,pixel_threshold=p_threshold,area_threshold=p_threshold)
    blobs_2 = img.find_blobs([thresholds],roi=(80,0,79,239),x_stride=1, y_stride=1,pixel_threshold=p_threshold,area_threshold=p_threshold)
    blobs_3 = img.find_blobs([thresholds],roi=(160,0,79,239),x_stride=1, y_stride=1,pixel_threshold=p_threshold,area_threshold=p_threshold)
    blobs_4 = img.find_blobs([thresholds],roi=(240,0,79,239),x_stride=1, y_stride=1,pixel_threshold=p_threshold,area_threshold=p_threshold)

    draw_divd(blobs_1)
    draw_divd(blobs_2)
    draw_divd(blobs_3)
    draw_divd(blobs_4)

    if blobs_1 and blobs_2:
        pass#print(sum(blobs_1.cx()))
    #img.draw_line(img.get_regression([thresholds],robust=True))
    lcd.display(img)

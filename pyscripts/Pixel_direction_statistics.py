#统计八个方向上的像素数量来分析图中有哪些岔路

from machine import SPI
import utime
import sensor, image, time,lcd
temp = sensor.QQVGA
sensor.reset(freq=30000000)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(temp)
sensor.skip_frames(time = 200)
sensor.run(1)
lcd.init(freq=15000000)
lcd.rotation(2)
clock = time.clock()
thresholds   = (0,100)
p_threshold=50
b1,b2=[0,0]
blobs_1,blobs_2,blobs_3,blobs_4=[0,0,0,0]
divid_x,divid_y =18,18
center,times,cen=0,1,0
cr=[([0] * divid_y) for i in range(divid_x)]
dir=[([0] * 5) for i in range(5)]
if temp == sensor.QVGA:win_x,win_y=320,240
elif temp == sensor.QQVGA:win_x,win_y=160,120
elif temp == sensor.B128X64:win_x,win_y=128,64
def fb(x,y,z):
    if img2.get_pixel(x,y) > z :cr[x][y]=0
    else :cr[x][y]=1
def find_dir():
    k,l=1,2
    for i in range(divid_x-2*(k+l-1)):
        for j in range(divid_y-2*(k+l-1)):
            if cr[i+1][j+1]==1:
                for dir_x in range(2*k+1):
                    for dir_y in range(2*k+1):
                        if cr[i+1+l*(dir_x-k)][j+1+l*(dir_y-k)]==1 \
                        and cr[i+1-l*(dir_x-k)][j+1-l*(dir_y-k)]==1:
                            dir[dir_y][dir_x]= dir[dir_y][dir_x]+1
    return dir

def find_zero():
    k,l=1,1
    for i in range(divid_x-2*(k+l-1)):
        for j in range(divid_y-2*(k+l-1)):
            if cr[i+1][j+1]==1:
                for dir_x in range(2*k+1):
                    for dir_y in range(2*k+1):
                        if cr[i+1+l*(dir_x-k)][j+1+l*(dir_y-k)]==1 \
                        and cr[i+1-l*(dir_x-k)][j+1-l*(dir_y-k)]==0:
                            dir[dir_y][dir_x]= dir[dir_y][dir_x]+1
    return dir
"""
def addition(i,j,k,l,addi):
    if cr[i+l*(0-k)+addi][j+l*(0-k)]==1 \
    and cr[i-l*(0-k)-addi][j-l*(0-k)]==1:
        dir[0][0]= dir[0][0]+1
    if cr[i+l*(2-k)-addi][j+l*(0-k)]==1 \
    and cr[i-l*(2-k)+addi][j-l*(0-k)]==1:
        dir[0][2]= dir[0][2]+1
    if cr[i+l*(0-k)][j+l*(0-k)+addi]==1 \
    and cr[i-l*(0-k)][j-l*(0-k)-addi]==1:
        dir[0][0]= dir[0][0]+1
    if cr[i+l*(2-k)][j+l*(0-k)+addi]==1 \
    and cr[i-l*(2-k)][j-l*(0-k)-addi]==1:
        dir[0][2]= dir[0][2]+1

def get_dir():
    k,l=1,5
    for i in range(1,divid_x-2*(k+l-1)-1):
        for j in range(1,divid_y-2*(k+l-1)-1):
            if cr[i+1][j+1]==1:
                k,l=1,5
                addition(i,j,k,l,0)
                addition(i,j,k,l,1)
                addition(i,j,k,l,2)
                addition(i,j,k,l,3)
                addition(i,j,k,l,4)

                k,l=1,2
                if cr[i+1+l*(0-k)][j+1+l*(1-k)]==1 \
                and cr[i+1-l*(0-k)][j+1-l*(1-k)]==1:
                    dir[1][0]= dir[1][0]+1
                if cr[i+1+l*(1-k)][j+1+l*(0-k)]==1 \
                and cr[i+1-l*(1-k)][j+1-l*(0-k)]==1:
                    dir[0][1]= dir[0][1]+1
    return dir
"""
def find_center():
    sum_x,sum_y=0,0
    times_x=0
    for i in range(divid_x):
        for j in range(divid_y):
            if cr[i][j]==1:
                sum_x=i+sum_x
                times_x=times_x+1
                sum_y=j+sum_y
    return sum_x/(times_x+1),times_x,sum_y/(times_x+1)

spi = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=3750000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=28, mosi=29, miso=30, cs0=27)
str_temp="1"
yita=2
sigma=190
state=0
while 1:
    clock.tick()
    img = sensor.snapshot()
    img2=img.mean_pooled(int(win_x/divid_x),int(win_y/divid_y))
    img3=img.get_statistics()
    img.draw_string(0,0,str_temp,scale=2)
    img.draw_string(40,0,str(state),scale=2)
    """
    img.draw_string(0,30,str(dir[0][0]+dir[4][4]+dir[1][1]+dir[2][2]+dir[3][3]),scale=3)
    img.draw_string(0,60,str(dir[0][2]+dir[1][2]+dir[2][2]+dir[3][2]+dir[4][2]),scale=3)
    img.draw_string(0,90,str(dir[0][4]+dir[1][3]+dir[2][2]+dir[3][1]+dir[4][0]),scale=3)
    img.draw_string(0,120,str(dir[2][0]+dir[2][1]+dir[2][2]+dir[2][3]+dir[2][4]+dir[2][4]),scale=3)
    """


    img.draw_string(0,20,"L"+str(dir[0][0]),scale=2)
    img.draw_string(0,40,"R"+str(dir[0][2]),scale=2)
    img.draw_string(0,60,"I"+str(dir[0][1]),scale=2)
    img.draw_string(0,80,"-"+str(dir[1][0]),scale=2)
    img.draw_string(0,100,str(times),scale=2)
    img.draw_string(0,120,str(center),scale=2)
    img.draw_cross(int(center*win_x/divid_x),int(cen*win_y/divid_y))
    img.draw_string(0,210,str(dir[0][0]-dir[0][2]),scale=3)
    img.draw_string(90,210,str(dir[0][1]-dir[1][0]),scale=3)
    dir=[([0] * 3) for i in range(3)]

    lcd.display(img)
    state=0
    for i in range(divid_x):
        for j in range(divid_y):
            fb(i,j,img3[0]-20)#70)
    find_zero()
    center,times,cen=find_center()
    if times>30:
        yita=(24-cen)/divid_y*center/6
        if center<divid_x/2-yita:
            str_temp='2'
        elif center>divid_x/2+yita:
            str_temp='0'
        else :
            str_temp='1'
    else : str_temp='x'
    dir[0][0]=(dir[0][0]*10)#*20//times)
    dir[0][2]=(dir[0][2]*10)#*20//times)
    dir[0][1]=(dir[0][1]*15)#*30//times)
    dir[1][0]=(dir[1][0]*15)#*100//times)
    if dir[0][0]>sigma:
        state=state+1
    if dir[0][2]>sigma:
        state=state+100
    if dir[1][0]>sigma:
        state=state+10
    if dir[0][1]>sigma:
        state=-state
    if abs(state) == 111:str_temp='Y'

    print(find_center())
    print(clock.fps())
    print(str_temp)
    print(dir)
    for lll in range(divid_y):
        print(cr[lll])

    spi.write(str_temp, cs=SPI.CS0)

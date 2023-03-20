from machine import SPI
import utime

from fpioa_manager import fm
from Maix import GPIO

io_led_red = 13
fm.register(io_led_red, fm.fpioa.GPIO0)

led_r=GPIO(GPIO.GPIO0, GPIO.OUT)


spi = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=3750000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=28, mosi=29, miso=30, cs0=27)
i=0
while 1:
    w = str(i%2)+'0'

    bf =  bytearray(8)
    spi.write(w, cs=SPI.CS0)
    #spi.readinto(buf, write=0x00, cs=SPI.CS0)
    utime.sleep_ms(100)
    #print(i)
    #print(buf)
    i=i+1
    led_r.value(i%2)


from fpioa_manager import fm

# need your connect hardware IO 9/10 to loopback
fm.register(9, fm.fpioa.UART1_TX, force=True)
fm.register(10, fm.fpioa.UART1_RX, force=True)
import time
from machine import UART

uart_A = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)

time.sleep_ms(100) # wait uart ready

uart_A.write("s")

while 1:

    while uart_A.any():
        read_data = uart_A.read()
        print(read_data)

"""
uart_A.deinit()
del uart_A
"""

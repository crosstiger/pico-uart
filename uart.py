import machine
from machine import Pin
from utime import sleep_ms

pin = Pin(22, Pin.OUT)
uart_buffer = machine.UART(0, 9600)
uart_buffer.init(9600, 8, None, 1)

uart_buffer.write("Hello World\n\r")

while True:
    try:
        if uart_buffer.any():
            data = uart_buffer.read().strip()
            print(data)
            if data == b'1':
                pin.on()
                uart_buffer.write("Relay turned ON\n\r")
            elif data == b'0':
                pin.off()
                uart_buffer.write("Relay turned OFF\n\r")
        sleep_ms(100)
    except KeyboardInterrupt:
        break
pin.off()
uart_buffer.deinit()
import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:11:p')

for i in range(10):
    print(i)
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)

led.write(0)


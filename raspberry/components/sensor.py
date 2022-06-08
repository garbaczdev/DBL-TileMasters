import smbus
import time

bus = smbus.SMBus(1)
address = 0x29


while True:
    for i in range(100):
        bear = bus.read_byte_data(address, 1)
        print(f"[Register {i}]:", bin(bear))
    time.sleep(1)
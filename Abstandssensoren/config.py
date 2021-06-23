#!/usr/bin/python

import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x40      #7 bit address (will be left shifted to add the read write bit
DEVICE_ADDRESS_NEW = 0x40
bus.write_byte_data(DEVICE_ADDRESS, 0xEC, 0xFF)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xC8, 0x00)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xC9, 0x45)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xCD, 0x10)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xCA, 0x01)
time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xCA, 0x00)
#time.sleep(5)
bus.write_byte_data(DEVICE_ADDRESS, 0xEF, 0x00)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xC8, 0x40)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xC8, 0x00)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xEE, 0x06)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xEF, 0x00)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xEC, 0xFF)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS, 0xEF, 0x03)
#time.sleep(1)
print bus.read_i2c_block_data(DEVICE_ADDRESS, 0x27)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS_NEW, 0xEF, 0x00)
#time.sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS_NEW, 0xEC, 0x7F)

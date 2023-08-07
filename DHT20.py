import smbus
import time

i2c = smbus.SMBus(1)
address = 0x38
set = [0xAC, 0x33, 0x00]
dat = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
time.sleep(0.1)
ret = i2c.read_byte_data(address, 0x71)
if ret != 0x18:
    exit

def DHT20():
    time.sleep(0.01)
    i2c.write_i2c_block_data(address, 0x00, set)
    time.sleep(0.08)
    dat = i2c.read_i2c_block_data(address, 0x00, 0x07)
    hum = dat[1] << 12 | dat[2] << 4 | ((dat[3] & 0xF0) >> 4)
    tmp = ((dat[3] & 0x0F) << 16) | dat[4] << 8 | dat[5]
    hum = hum / 2**20 * 100
    tmp = tmp / 2**20 * 200 - 50
    return round(tmp,1),round(hum,1)

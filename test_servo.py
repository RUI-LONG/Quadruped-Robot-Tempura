import time
from Raspi_I2C.matrix_servo_extension import MatrixServoExtension

device = MatrixServoExtension()
print("Device Connected:", device.begin())
time.sleep(1)

try:
    for i in range(1, 9):
        device.setAngle(i, 90)
    time.sleep(500)

except :
    device.close()

device.close()
print("Device Closed")
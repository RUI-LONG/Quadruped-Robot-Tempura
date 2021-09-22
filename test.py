from .Raspi_I2C.MatrixServoExtension import MatrixServoExtension

device = MatrixServoExtension()
print("Device Connected:", device.begin())
time.sleep(1)
# for i in range(1, 9):
#     device.setAngle(i, 90)
device.setAngle(1, 90)

time.sleep(2)
device.setAngle(2, 90)

time.sleep(20)

device.close()

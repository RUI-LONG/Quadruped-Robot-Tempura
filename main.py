import time
from Raspi_I2C.matrix_servo_extension import MatrixServoExtension
from Movement.movement import Skills

device = MatrixServoExtension()
skill = Skills(device)
print("Device Connected:", device.begin())
time.sleep(2)

try:
    # skill.layDown()
    # time.sleep(2)
    # skill.standUp()

    time.sleep(20)

except KeyboardInterrupt:
    pass
        
except Exception as e:
    print(e)

device.close()
time.sleep(1)
print("Device Closed")
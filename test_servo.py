import time
from Raspi_I2C.matrix_servo_extension import MatrixServoExtension
from Movement.movement import Skills

device = MatrixServoExtension()
skill = Skills(device)
print("Device Connected:", device.begin())
time.sleep(2)
_body = {"LF": skill.LeftF, "lf": skill.LeftF, "LB": skill.LeftB, "lb": skill.LeftB,
    "RF": skill.RightF, "rf": skill.RightF, "RB": skill.RightB, "rb": skill.RightB,
    "su": skill.standUp, "ld":skill.layDown, "ld2":skill.layDown2 }

while True:
    try:
        _input = input("Input Angle:").split(" ")
        if len(_input) == 1:
            _body[_input[0]]()
        else:
            if isinstance(_input[2], int):
                _body[_input[0]](int(_input[1]), int(_input[2]))
            else:
                _body[_input[0]](int(_input[1]), -1)
            
    except:
        break

# time.sleep(2)
device.close()
time.sleep(1)
print("Device Closed")
import time
from Raspi_I2C.matrix_servo_extension import MatrixServoExtension
from Movement.movement import Skills

device = MatrixServoExtension()
skill = Skills(device)

device_status = device.begin()
if device_status:
    time.sleep(2)
    _body = {
        "lf": skill.LeftF, "lb": skill.LeftB, "rf": skill.RightF,  "rb": skill.RightB, "hd": skill.headTurn,

        "sb": skill.standBy, "su": skill.standUp, "pu": skill.pushUp, "ld":skill.layDown,
        "sd": skill.sitDown,  "shr": skill.shakeRightHand, "shl": skill.shakeLeftHand,
        "stf": skill.stretchF, "ca": skill.crazy, "wa": skill.walk, "yo": skill.yoga, "wu":skill.warmUp,
        # TODO
        "gd":skill.getDown, 
        "t1": skill.t1, "t2": skill.t2, "t3": skill.t3, "t4": skill.t4,
    }

    skill.standBy(50)

    while True:
        try:
            _input = input("Input Command:").split(" ")
            if len(_input) == 1:
                _body[_input[0]]()
            elif len(_input) == 3:
                _body[_input[0]](int(_input[1]), int(_input[2]))
            else:
                _body[_input[0]](int(_input[1]))

            print("rf:", skill.rf_a, skill.rf_h, ",",
                    "rb:", skill.rb_a, skill.rb_h)
            print("lf:", skill.lf_a, skill.lf_h, ",",
                    "lb:", skill.lb_a, skill.lb_h)
        except KeyboardInterrupt:
            break
        except KeyError:
            print("KeyError")
            pass
        except Exception as e:
            print(e)
            break

device.close()
time.sleep(2)
print("Device Closed")

#!/usr/bin/env python3

README = """
This basic demo demonstrates the control the user have on how and when events are triggered,
by simply printing to the console event information each time an event is triggered. 

This control is defined with the following parameters of a pose-action:
- trigger : possible values: 
    - enter (default): an event is triggered once, when the pose begins,
    - enter_leave : two events are triggered, one when the pose begins and one when the pose ends,
    - periodic : events are triggered periodically as long as the pose stands.
                 The period is given by the parameter 'next_trigger_delay' in s.
    - continuous : events are triggered on every frame.

- first_trigger_delay: because false positive happen in pose recognition, 
you don't necessarily want to trigger an event on the first frame where the pose is recognized.
The 'first_trigger_delay' in seconds specifies how long the pose has to stand before triggering
an initial event.

"""
import time
from Movement.movement import Skills
from Raspi_I2C.matrix_servo_extension import MatrixServoExtension
from depthai_hand_tracker.HandController import HandController

device = MatrixServoExtension()
skill = Skills(device)
print("Device Connected:", device.begin())
time.sleep(2)

def StandOrSit(event):
    event.print_line() 
    hand_ang = event.hand.rotation
    print(hand_ang)
    if hand_ang > 1 or hand_ang < -1:
        # print("sit")
        skill.sitDown()
    else:
        # print("stand")
        skill.standUp()
def shakeRightHand(event):
    event.print_line() 
    print("right")
    skill.shakeRightHand()

def shakeLeftHand(event):
    event.print_line() 
    print("left")
    skill.shakeLeftHand()

def stop(event):
    pass

def trackBall(event):
    pass

def walkForward(event):
    pass

def walkBackward(event):
    pass

def shakeHand(event):
    pass


# ALL_POSES = ["ONE","TWO","THREE","FOUR","FIVE","FIST","SEVEN","OK"]

config = {
    'renderer' : {'enable': False},
    
    'pose_actions' : [
        {'name': 'StandOrSit', 'pose':['ONE', 'SEVEN'], 'callback': 'StandOrSit', "trigger":"enter", "first_trigger_delay":0.2, "next_trigger_delay": 0.2},
        {'name': 'shakeLeftHand', 'pose': 'FIVE', 'hand':'left', 'callback': 'shakeLeftHand', "trigger":"enter", "first_trigger_delay":0.2, "next_trigger_delay": 3},
        {'name': 'shakeRightHand', 'pose': 'FIVE', 'hand':'right', 'callback': 'shakeRightHand', "trigger":"enter", "first_trigger_delay":0.2, "next_trigger_delay": 3},

        
    ]
}

try:
    skill.standBy()
    HandController(config).loop()
except KeyboardInterrupt:
    pass
device.close()
time.sleep(2)
print("Device Closed")
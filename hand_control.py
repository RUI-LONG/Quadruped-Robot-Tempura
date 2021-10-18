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
    hand_ang = event.hand.rotation
    if hand_ang > 1 or hand_ang < -1:
        skill.sitDown()
    else:
        skill.standUp()

def pushUpOrNot(event):
    hand_ang = event.hand.rotation
    if hand_ang > 1 or hand_ang < -1:
        skill.pushUp()
    else:
        skill.standUp()

def shakeRightHand(event):
    event.print_line() 
    skill.shakeRightHand()

def shakeLeftHand(event):
    event.print_line() 
    skill.shakeLeftHand()

def stretch(event):
    skill.stretchF()

def standBy(event):
    skill.standBy()

def carzy(event):
    skill.crazy()

def yoga(event):
    skill.yoga()

def trackBall(event):
    pass

def walkForward(event):
    pass

def walkBackward(event):
    pass


# ALL_POSES = ["ONE","TWO","THREE","FOUR","FIVE", "ROCK", "FIST","SEVEN","OK","FUCK1","FUCK2"]
# Registed = ["THREE", "FOUR", "OK"]


config = {
    'renderer' : {'enable': False},
    
    'pose_actions' : [
        {'name': 'StandOrSit', 'pose':['ONE', 'SEVEN'], 'hand':'left', 'callback': 'StandOrSit', "trigger":"enter", 
            "first_trigger_delay":0.1, "next_trigger_delay": 0},

        {'name': 'pushUpOrNot', 'pose':['ONE', 'SEVEN'], 'hand':'right', 'callback': 'pushUpOrNot', "trigger":"enter", 
            "first_trigger_delay":0.1, "next_trigger_delay": 0},

        {'name': 'stretch', 'pose':'TWO', 'callback': 'stretch', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'yoga', 'pose':'ROCK', 'callback': 'yoga', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'carzy', 'pose': ['FUCK1', 'FUCK2'], 'callback': 'carzy', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'shakeLeftHand', 'pose': 'FIVE', 'hand':'left', 'callback': 'shakeLeftHand', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},
        {'name': 'shakeRightHand', 'pose': 'FIVE', 'hand':'right', 'callback': 'shakeRightHand', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0}
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

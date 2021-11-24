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
from Movement.pid import PID
from Raspi_I2C.matrix_servo_extension import MatrixServoExtension
from depthai_hand_tracker.HandController import HandController

from numpy import interp

device = MatrixServoExtension()
skill = Skills(device)

status = device.begin()
print("Device Connected:", status)
pid = PID(1, 0.01, 0.01)
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
        skill.standBy(70)

def shakeRightHand(event):
    # event.print_line() 
    skill.shakeRightHand()

def shakeLeftHand(event):
    skill.shakeLeftHand()

def stretch(event):
    skill.stretchF()

def standBy(event):
    skill.standBy()

def carzy(event):
    skill.crazy()

def yoga(event):
    skill.yoga()

def walk(event):
    skill.walk(1)

def trackBall(event):
    pass

def warmUp(event):
    skill.warmUp()
    
def traceFist(event):
    # TODO
    # cam_width = 1152
    # cam_height = 648
    # error = int((576 - int(event.hand.rect_x_center_a))/20)
    # output = pid.update(error, debug=True)
    # sevro_adjust = int(interp(output,[-400, 400],[-90, 90]))
    # print(sevro_adjust)
    # print("X: ", int(event.hand.rect_x_center_a), "Y: ",int(event.hand.rect_y_center_a))
    pass

def stop(event):
    skill.standBy(50)


# ALL_POSES = ["ONE","TWO","THREE","FOUR","FIVE", "ROCK", "FIST","SEVEN","NICE","FUCK1","FUCK2"]
# Registed = ["THREE", "FOUR", "NICE"]

config = {
    'renderer' : {'enable': False},
    
    'pose_actions' : [
        {'name': 'StandOrSit', 'pose':['ONE', 'SEVEN'], 'hand':'left', 'callback': 'StandOrSit', "trigger":"enter", 
            "first_trigger_delay":0.15, "next_trigger_delay": 0},

        {'name': 'pushUpOrNot', 'pose':['ONE', 'SEVEN'], 'hand':'right', 'callback': 'pushUpOrNot', "trigger":"enter", 
            "first_trigger_delay":0.15, "next_trigger_delay": 0},

        {'name': 'stretch', 'pose':'TWO', 'callback': 'stretch', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'yoga', 'pose':'ROCK', 'callback': 'yoga', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'carzy', 'pose': ['FUCK1', 'FUCK2'], 'callback': 'carzy', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'shakeLeftHand', 'pose': 'FIVE', 'hand':'left', 'callback': 'shakeLeftHand', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},
        {'name': 'shakeRightHand', 'pose': 'FIVE', 'hand':'right', 'callback': 'shakeRightHand', "trigger":"enter", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'walk', 'pose': 'FOUR', 'callback': 'walk', "trigger":"periodic", 
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'stop', 'pose': 'FIST', 'callback': 'stop', "trigger":"enter",
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        {'name': 'warmUp', 'pose': 'NICE', 'callback': 'warmUp', "trigger":"enter",
            "first_trigger_delay":0.2, "next_trigger_delay": 0},

        # {'name': 'traceFist', 'pose': 'FIST', 'hand':'right', 'callback': 'traceFist', "trigger":"continuous",
        #     "first_trigger_delay":0, "next_trigger_delay": 0},

    ]
}

try:
    if status:
        skill.standBy()
        HandController(config).loop()
except:
    device.close()
    pass

time.sleep(2)
print("Device Closed")

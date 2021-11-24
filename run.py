import os
from time import time
from gpiozero import Button

button = Button(5, hold_time=2)

def run():
    print("Start")
    os.system("python3 /home/pi/Desktop/tempura/hand_control.py")

while True:
    try:
        button.when_pressed = run
    except KeyboardInterrupt:
        break
    except:
        break

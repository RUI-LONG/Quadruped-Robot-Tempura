import time
from gpiozero import AngularServo

try:
    from .body import Body
except ModuleNotFoundError:
    from body import Body

class Skills(Body):
    def __init__(self, device):
        self.head_middle = 80
        self.device = device
        self.right_f_arm = 1
        self.right_f_hand = 2
        self.left_f_arm = 3
        self.left_f_hand = 4
        self.left_b_arm = 5
        self.left_b_hand = 6
        self.right_b_arm = 7
        self.right_b_hand = 8

        # Store angle of Servos
        self.rf_a = -1
        self.rf_h = -1
        self.rb_a = -1
        self.rb_h = -1
        self.lf_a = -1
        self.lf_h = -1
        self.lb_a = -1
        self.lb_h = -1

        self.head = AngularServo(17, min_angle=0, max_angle=180)
        self.head.angle = self.head_middle
    
    def headTurn(self, ang=80):
        if ang > 180:
            ang = 179
        if ang < 0:
            ang = 0
        self.head.angle = ang

    def standUp(self):
        self.LeftF(130, 60)
        self.RightF(60, 130)
        self.LeftB(-1, 50)
        self.RightB(-1, 130)
        time.sleep(0.2)
        self.LeftB(115, -1)
        self.RightB(60, -1)

    def sitDown(self):
        self.LeftB(180, 170)
        self.RightB(0, 10)
        time.sleep(0.1)
        self.LeftF(130, 60)
        self.RightF(60, 130)

    def layDown(self):
        self.LeftF(-1, 170)
        self.RightF(-1, 10)
        self.LeftB(-1, 170)
        self.RightB(-1, 10)
        time.sleep(0.2)
        self.LeftF(180, -1)
        self.RightF(0, -1)
        self.LeftB(180, -1)
        self.RightB(0, -1)
    
    def getDown(self):
        self.LeftF(-1, 80)
        self.RightF(-1, 110)
        self.LeftB(-1, 0)
        self.RightB(-1, 170)
        time.sleep(0.1)
        self.LeftF(60, -1)
        self.RightF(130, -1)
        self.LeftB(95, -1)
        self.RightB(80, -1)
        # next: standBy

    def standBy(self, ang=30):
        self.LeftF(-1, 170-ang)
        self.RightF(-1, 10+ang)
        self.LeftB(-1, 170-ang-5)
        self.RightB(-1, 10+ang)
        time.sleep(0.05)
        
        if ang >= 40:
            ang = 40
        self.LeftF(180-ang, -1)
        self.RightF(0+ang, -1)
        self.LeftB(180-ang, -1)
        self.RightB(0+ang, -1)

    def shakeRightHand(self, cnt=2):
        self.LeftB(180, 170)
        self.RightB(0, 10)
        self.LeftF(130, 60)
        self.RightF(60, 130)
        time.sleep(0.2)
        for i in range(cnt):
            for ang in range(110, 149, 1):
                self.RightF(ang, -1)
                time.sleep(0.015)

            for ang in range(149, 109, -1):
                self.RightF(ang, -1)
                time.sleep(0.015)
        self.RightF(60, 130)
        time.sleep(0.5)

    def shakeLeftHand(self, cnt=2):
        self.LeftB(180, 160)
        self.RightB(0, 10)
        self.LeftF(130, 60)
        self.RightF(60, 130)
        time.sleep(0.2)

        for i in range(cnt):
            for ang in range(40, 90, 1):
                self.LeftF(ang, -1)
                time.sleep(0.015)

            for ang in range(90, 40, -1):
                self.LeftF(ang, -1)
                time.sleep(0.015)
        self.LeftF(130, 60)
        time.sleep(0.5)

    def crazy(self, cnt=5):
        # Warning! Call This Function will let all of servos release.
        for i in range(5):
            self.standBy(0)
            time.sleep(0.15)
            self.standBy(50)
            time.sleep(0.15)
        self.standBy()
        time.sleep(0.5)

    def walk(self, cnt=1):
        self.LeftF(150, 140)
        self.RightF(30, 40)
        self.LeftB(150, 140)
        self.RightB(30, 40)

        for i in range(cnt):
            self.LeftF(90, 90) # 150, 140
            self.LeftB(180, 150) # 150, 140
            self.RightB(90, 0) # 30, 40
            time.sleep(0.1)
            self.RightF(0, 50) # 30, 40
            self.RightB(90, 30) # 30, 40
            time.sleep(0.1)
            self.RightF(-1, 10) # 30, 40
            time.sleep(0.1)
            time.sleep(0.1)
            self.RightB(-1, 90) # 30, 40

            self.LeftF(180, 150) # 150, 140
            self.RightB(90, 90) # 30, 40
            time.sleep(0.1) 
            self.RightF(90, 0) # 30, 40
            self.LeftB(180, 130) # 150, 140
            time.sleep(0.1)
            self.LeftB(-1, 170) # 150, 140
            time.sleep(0.1)
            time.sleep(0.1)
            self.RightF(-1, 90) # 30, 40

            self.RightF(90, 90) # 30, 40
            self.RightB(0, 30) # 30, 40
            self.LeftB(90, 180) # 150, 140
            time.sleep(0.1)
            self.LeftF(180, 130) # 150, 140
            self.LeftB(90, 150) # 150, 140
            time.sleep(0.1)
            self.LeftF(-1, 170) # 150, 140
            time.sleep(0.1)
            time.sleep(0.1)
            self.LeftB(-1, 90) # 150, 140
            
            self.LeftB(90, 90) # 150, 140
            self.RightF(0, 30) # 30, 40
            time.sleep(0.1)
            self.LeftF(90, 180) # 150, 140
            self.RightB(0, 50) # 30, 40
            time.sleep(0.1)
            self.RightB(-1, 10) # 30, 40
            time.sleep(0.1)
            time.sleep(0.1)
            self.LeftF(-1, 90) # 150, 140

    def pushUp(self, cnt=3):
        self.standUp()
        time.sleep(0.5)
        self.LeftB(180, -1)
        self.RightB(0, -1)
        time.sleep(0.1)

        self.LeftB(-1, 50)
        self.RightB(-1, 130)

        # front
        self.RightF(-1, 100)
        self.LeftF(-1, 80)
        time.sleep(0.1)
        self.RightF(30, -1)
        self.LeftF(150, -1)

        time.sleep(0.3)

        for i in range(cnt):
            for ang in range(30, 0, -1):
                self.LeftF(180-ang, 170-ang*3)
                self.RightF(ang, ang*3+10)
                time.sleep(0.001)

            for ang in range(0, 30, 1):
                self.LeftF(180-ang, 170-ang*3)
                self.RightF(ang, ang*3+10)
                time.sleep(0.001)
        self.standBy()
        time.sleep(0.2)

    def warmUp(self, cnt=5):
        self.standBy(50)
        for _ in range(cnt):
            self.LeftF(-1, 132)
            self.LeftB(-1, 115)
            self.RightF(-1, 60)
            self.RightB(-1, 40)
            time.sleep(0.15)
            self.RightF(-1, 40)
            self.RightB(-1, 60)
            self.LeftF(-1, 115)
            self.LeftB(-1, 132)
            time.sleep(0.15)
        self.standBy(50)
        time.sleep(0.2)

    def stretchF(self):
        self.standUp()
        time.sleep(0.5)
        for ang in range(0, 60, 1):
            self.LeftF(150-int(ang*2)+10, 140-ang)
            self.RightF(30+int(ang*2)-10, 40+ang)
            time.sleep(0.005)
        time.sleep(0.5)
        self.standBy()
        time.sleep(0.5)

    def yoga(self):
        self.standBy(50)
        time.sleep(0.5)
        self.RightB(40, 180)
        time.sleep(0.6)
        self.LeftB(120, 140)
        self.RightF(60, 40)
        self.LeftF(120, 140)
        time.sleep(0.5)

        for ang in range(0, 40, 1):
            self.LeftF(120-ang*2, 140-ang*2)
            self.RightB(40-ang, 180-ang)
            time.sleep(0.01)
        time.sleep(2)

        # Change Side
        self.layDown()
        time.sleep(0.5)
        self.standBy(50)
        time.sleep(0.4)
        self.LeftB(140, 0)
        time.sleep(0.6)
        self.RightB(60, 30)
        self.LeftF(120, 140)
        self.RightF(60, 40)
        time.sleep(0.5)

        for ang in range(0, 40, 1):
            self.RightF(60+ang*2, 40+ang*2)
            self.LeftB(140+ang, ang)
            time.sleep(0.01)
        time.sleep(2)

        self.layDown()
        time.sleep(0.5)

    # Test code
    def t1(self):
        for _ in range(5):
            self.standBy(10)
            time.sleep(1)
            self.standBy(70)
            time.sleep(1)

    def t2(self):
        self.LeftB(170, 130)
        time.sleep(0.1*2)
        self.RightF(70, 130)
        self.RightB(70, 80)
        time.sleep(0.1*2)
        self.LeftF(150, 160)

    def t3(self):
        self.RightF(10, 50)
        time.sleep(0.1*2)
        self.LeftF(110, 100)
        self.RightB(70, 130)
        time.sleep(0.1*2)
        self.LeftB(150, 160)


    def t4(self):
        self.RightB(10, 50)
        time.sleep(0.1*2)
        self.LeftF(110, 70)
        self.LeftB(110, 100)
        time.sleep(0.1*2)
        self.RightF(40, 20)
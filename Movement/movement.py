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
        self.head = AngularServo(17, min_angle=0, max_angle=180)
        self.head.angle = self.head_middle

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
        self.LeftB(-1, 170-ang)
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
        for i in range(5):
            self.standBy(0)
            time.sleep(0.15)
            self.standBy(50)
            time.sleep(0.15)
        self.standBy()
        time.sleep(1)

    def jump(self):
        # TODO
        self.standBy()
        time.sleep(1)

        ang = 90
        # self.LeftF(-1, 170-ang)
        # self.RightF(-1, 10+ang)
        # self.LeftB(-1, 170-ang)
        # self.RightB(-1, 10+ang)
        # time.sleep(0.03)
        
        # self.LeftF(180-ang, -1)
        # self.RightF(0+ang, -1)
        # self.LeftB(180-ang, -1)
        # self.RightB(0+ang, -1)

        self.LeftF(-1, 60)
        self.RightF(-1, 130)
        self.LeftB(-1, 50)
        self.RightB(-1, 130)

        time.sleep(0.01)
        self.LeftB(115, -1)
        self.RightB(60, -1)
        self.LeftF(130, -1)
        self.RightF(60, -1)

    def walk(self, cnt=5):
        self.LeftF(150, 140)
        self.RightF(30, 40)
        self.LeftB(150, 140)
        self.RightB(30, 40)

        for i in range(5):
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

    def warmUp(self, cnt=2):
        pass

    def stretchF(self):
        self.standUp()
        time.sleep(0.5)
        for ang in range(0, 60, 1):
            self.LeftF(150-int(ang*2)+10, 140-ang)
            self.RightF(30+int(ang*2)-10, 40+ang)
            time.sleep(0.005)
        time.sleep(0.5)
        self.standBy()
        time.sleep(1)

    def stretchB(self):
        # TODO
        pass
        self.standUp()
        time.sleep(0.5)
        # for ang in range(0, 60, 1):
        #     self.LeftF(150-int(ang*1.5), 140-ang)
        #     self.RightF(30+int(ang*1.5), 40+ang)
        #     time.sleep(0.005)

    def yoga(self):
        self.standBy()
        
        self.LeftB(120, 140)
        self.RightF(60, 40)
        time.sleep(0.15)
        
        self.RightB(0, 180)
        time.sleep(0.15)
        for ang in range(0, 60, 1):
            self.LeftF(160-ang*2, 140-ang)

        for _ in range(6):
            for ang in range(0, 40, 1):
                self.LeftF(-1, 10+ang)
                self.RightB(-1, 180+ang)
                time.sleep(0.001)

            for ang in range(40, 0, -1):
                self.LeftF(-1, 50+ang)
                self.RightB(-1, 140+ang)
                time.sleep(0.001)
        self.standBy()
        time.sleep(1)


    def t1(self):
        self.LeftF(150, 130)
        time.sleep(0.1*2)
        self.LeftB(130, 80)
        self.RightF(70, 80)
        time.sleep(0.1*2)
        self.RightB(40, 20)

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

    def t5(self):
        for _ in range(20):
            self.t1()
            self.t2()
            self.t3()
            self.t4()

    def t6(self):
        for i in range(15):
            self.LeftF(170, 130)
            time.sleep(0.3)
            self.LeftF(150, 160)
            time.sleep(0.1)
            self.LeftF(110, 100)
            time.sleep(0.2)
            self.LeftF(110, 70)
            time.sleep(0.1)

    def t7(self):
        self.LeftF(150, 140)
        self.RightF(30, 40)
        self.LeftB(150, 140)
        self.RightB(30, 40)
        ang = 10
        ang2 = 20
        for i in range(5):
            self.LeftF(90+ang2, 90-ang) # 150, 140
            time.sleep(0.1)
            time.sleep(0.1)
            time.sleep(0.1)
            time.sleep(0.1)

            self.LeftF(180, 150) # 150, 140
            time.sleep(0.1) 
            time.sleep(0.1)
            time.sleep(0.1)
            time.sleep(0.1)

            time.sleep(0.1)
            self.LeftF(180, 130-ang) # 150, 140
            time.sleep(0.1)
            self.LeftF(-1, 170-ang) # 150, 140
            time.sleep(0.1)
            time.sleep(0.1)
            
            time.sleep(0.1)
            self.LeftF(90+ang2, 180-ang) # 150, 140
            time.sleep(0.1)
            time.sleep(0.1)
            time.sleep(0.1)
            self.LeftF(-1, 90-ang) # 150, 140
            

    def t8(self):
        self.LeftF(150, 140)
        self.RightF(30, 40)
        self.LeftB(150, 140)
        self.RightB(30, 40)

        for i in range(5):
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
            
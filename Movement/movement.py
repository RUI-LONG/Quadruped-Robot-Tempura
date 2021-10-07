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
        self.LeftB(90, -1)
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

    def test(self):
        self.standUp()
        # lf 60 80

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

        time.sleep(0.03)
        self.LeftB(115, -1)
        self.RightB(60, -1)
        self.LeftF(130, -1)
        self.RightF(60, -1)

    def walk(self, cnt=5):
        pass

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
        # TODO
        # for _ in range(cnt):
        #     self.RightB(40, 70)
        #     self.LeftF(140, 110)

        #     self.RightF(0, 10)
        #     self.LeftB(180, 170)
        #     time.sleep(0.2)

        #     self.RightB(0, 10)
        #     self.LeftF(180, 170)

        #     self.RightF(40, 70)
        #     self.LeftB(140, 110)
        #     time.sleep(0.2)
            
        # self.RightB(0, 10)
        # self.LeftF(180, 170)
        # self.RightF(0, 10)
        # self.LeftB(180, 170)
        pass

    def stretchF(self, ):
        pass

    def stretchB(self, ):
        pass

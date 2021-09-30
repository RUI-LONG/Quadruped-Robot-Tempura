import time
try:
    from .body import Body
except ModuleNotFoundError:
    from body import Body

class Skills(Body):
    def __init__(self, device):
        self.device = device
        self.left_f_arm = 1
        self.left_f_hand = 2
        self.right_f_arm = 3
        self.right_f_hand = 4
        self.left_b_arm = 5
        self.left_b_hand = 6
        self.right_b_arm = 7
        self.right_b_hand = 8

    def standUp(self):
        self.LeftB(110, 50)
        self.RightB(60, 130)
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
        

    def shakeHand(self, cnt=4):
        pass

    def test(self, cnt=5):
        for _ in range(cnt):
            self.standBy(0)
            time.sleep(0.4)
            self.standBy(30)
            time.sleep(0.4)

    def pushUp(self, cnt=5):
        pass

    def warmUp(self, cnt=5):
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

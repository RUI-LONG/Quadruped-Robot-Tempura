import time

class Body():
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
            
    def LeftF(self, arm_angle, hand_angle, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.left_f_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.left_f_arm, arm_angle)


    def RightF(self, arm_angle, hand_angle, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.right_f_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.right_f_arm, arm_angle)


    def LeftB(self, arm_angle, hand_angle, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.left_b_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.left_b_arm, arm_angle)


    def RightB(self, arm_angle, hand_angle, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.right_b_arm, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.right_b_hand, arm_angle)

    def standUp(self):
        self.LeftF(90, 90)
        self.RightF(90, 90)

        self.LeftB(90, 90)
        self.RightB(90, 90)


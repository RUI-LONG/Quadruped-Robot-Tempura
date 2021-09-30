import time

class Body():
    def __init__(self):
        pass
            
    def LeftF(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.left_f_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.left_f_arm, arm_angle)

    def RightF(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.right_f_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.right_f_arm, arm_angle)

    def LeftB(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.left_b_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.left_b_arm, arm_angle)

    def RightB(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.device.setAngle(self.right_b_arm, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.device.setAngle(self.right_b_hand, arm_angle)

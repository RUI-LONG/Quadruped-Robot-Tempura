import time

class Body():
    def __init__(self):
        pass

    def LeftF(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.lf_h = hand_angle
            self.device.setAngle(self.left_f_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.lf_a = arm_angle
            self.device.setAngle(self.left_f_arm, arm_angle)

    def RightF(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.rf_h = hand_angle
            self.device.setAngle(self.right_f_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.rf_a = arm_angle
            self.device.setAngle(self.right_f_arm, arm_angle)

    def LeftB(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.lb_h = hand_angle
            self.device.setAngle(self.left_b_hand, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.lb_a = arm_angle
            self.device.setAngle(self.left_b_arm, arm_angle)

    def RightB(self, arm_angle, hand_angle=-1, t=0):
        if hand_angle != -1:
            self.rb_a = hand_angle
            self.device.setAngle(self.right_b_arm, hand_angle)
        time.sleep(t / 1000)
        if arm_angle != -1:
            self.rb_h = arm_angle
            self.device.setAngle(self.right_b_hand, arm_angle)

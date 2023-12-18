# 游戏建模
from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self, face, body, arm, leg):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %sm, %s, %s" %(self.face, self.body, self.arm, self.leg)

class PalyerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


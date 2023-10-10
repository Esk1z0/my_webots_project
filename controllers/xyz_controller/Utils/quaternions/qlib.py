import math
import numpy as np

class qlib:
    def __init__(self):
        pass

    def norm(self, quaternion):
        return math.sqrt(sum(componente ** 2 for componente in quaternion))

    def complementary(self, quaternion):
        result = quaternion
        for elemento in len(quaternion):
            if elemento > 0:
                result[elemento] = -quaternion[elemento]

        return result

    def inverse(self, quaternion):
        return (self.complementary(quaternion)/self.norm(quaternion))

    def product(self, quaternion1, quaternion2):
        array_2 = np.array(quaternion1)
        array_2 = []






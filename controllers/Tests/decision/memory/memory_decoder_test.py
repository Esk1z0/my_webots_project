import unittest
from controllers.xyz_controller.decision.memory.memory import Memory
from utils.EData import EData

class MyTestCase(unittest.TestCase):
    def test_something(self):
        mem = Memory()
        x = {EData.SECURITY_DATA : 'key'}
        y = mem.decode_command(x)
        print(y)
        self.assertEqual(y, 'value')  # add assertion here


if __name__ == '__main__':
    unittest.main()

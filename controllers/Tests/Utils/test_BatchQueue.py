import unittest
from controllers.xyz_controller.Utils.BatchQueue import BatchQueue

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion
    def test_concurrency(self):
        queue = BatchQueue()
        queue.dequeue()
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()

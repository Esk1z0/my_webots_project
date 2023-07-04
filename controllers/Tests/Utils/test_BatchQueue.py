import unittest
from controllers.xyz_controller.utils.batch_queue import BatchQueue
from time import sleep

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion
    def test_concurrency(self):
        queue = BatchQueue(2, 0.1)
        queue.start()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        print(queue.qsize())

        sleep(0.1)
        queue.stop()
        sleep(0.3)

        print(queue.qsize())
        self.assertEqual(queue.qsize(), 1)
    def test_run_stop(self):
        queue = BatchQueue()
        queue.start()
        sleep(0.1)
        print("a")
        queue.stop()
        sleep(0.3)
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()

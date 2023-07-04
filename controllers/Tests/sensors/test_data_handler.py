import unittest
from controllers.xyz_controller.utils.batch_queue import BatchQueue
from controllers.xyz_controller.sensors.data_handler import DataHandler


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_start_stop(self):
        camera = CameraDummy()
        batch = BatchQueue(-1, 0.01)

        camera_handler = DataHandler(camera, batch, ProcessDummy())

        camera_handler.start()
        camera_handler.stop()

        self.assertEqual(True, True)

class CameraDummy():
    def getImage(self):
        pass
class ProcessDummy():
    def process_data(self, data):
        pass

if __name__ == '__main__':
    unittest.main()

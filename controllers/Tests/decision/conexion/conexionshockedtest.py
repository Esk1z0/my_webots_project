import unittest
import socket

class MyTestCase(unittest.TestCase):
    UDP_IP = "127.0.0.1"  # Escucha en todas las interfaces de red
    UDP_PORT = 10000  # Puerto en el que escuchar

    def test_something(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((MyTestCase.UDP_IP, MyTestCase.UDP_PORT))

        print("Escuchando en {}:{}".format(MyTestCase.UDP_IP, MyTestCase.UDP_PORT))

        while True:
            data, addr = sock.recvfrom(1024)  # Tamaño máximo del mensaje a recibir
            print("Mensaje recibido desde {}: {}".format(addr, data.decode("utf-8")))

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

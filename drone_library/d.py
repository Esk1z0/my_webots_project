import mmap
from Mmap_Semaphore import BinarySemaphore
import time

b = BinarySemaphore(name="Hola")
# Abrir el archivo de memoria compartida
shm = mmap.mmap(-1, 10, "shared_memory")

data = b''
t = time.monotonic()
while True:
    while b.is_write_open():
        pass
    shm.seek(0)
    chunk = shm.read()
    print(chunk)
    data += chunk
    b.write_open()
    if chunk == b'\x00'*10:
        break

print('tiempo: ' + str(time.monotonic() - t))
print("Datos recibidos:", data.decode())

# Cerrar la memoria compartida
shm.close()
from controller import Robot
def prueba():
    robot = Robot()

    gyro = robot.getGyro("gyro")
    gyro.enable(10)

    while robot.step(10) != -1:
        gyro_values = gyro.getValues()
        print("Gyro values: ", gyro_values)


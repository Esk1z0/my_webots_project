from enum import Enum


class EInput(Enum):
    IMUPosition = "IMUPosition"
    IMUAngularVel = "IMUAngularVel"
    IMUAngularAccel = "IMUAngularAccel"
    DistanceSensor = "DistanceSensor"
    CameraDepth = "CameraDepth"
    CameraRecognition = "CameraRecognition"
    TEXT = "TEXT"

    TimeInterval = "TIMEINTERVAL"


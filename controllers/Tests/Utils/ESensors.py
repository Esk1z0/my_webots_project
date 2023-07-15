from enum import Enum


class EInput(Enum):
    IMUPosition = "IMUPosition"
    IMUAngularVel = "IMUAngularVel"
    IMUAngularAccel = "IMUAngularAccel"
    CameraDepth = "CameraDepth"
    CameraRecognition = "CameraRecognition"
    TEXT = "TEXT"


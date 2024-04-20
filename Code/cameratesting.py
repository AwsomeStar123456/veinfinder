from picamera2 import Picamera2, Preview
from libcamera import controls
import cv2 as cv
import numpy as np
import time
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL, x=50, y=100, width=640, height=480)
picam2.start()
picam2.set_controls({"ExposureTime": 50000, "AnalogueGain":2.0, "Contrast": 2.0, "AeEnable": False, "AwbEnable": False})
for i in range(12):
	time.sleep(100)
	picam2.capture_file("Semrah" + str(i) + ".jpg")

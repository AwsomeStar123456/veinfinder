from picamera2 import Picamera2, Preview
from libcamera import controls
import cv2 as cv
import numpy as np
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
picam2.set_controls({"ExposureTime": 50000, "AnalogueGain":2.0, "Contrast": 2.0, "AeEnable": False, "AwbEnable": False})

cv.namedWindow('Vein Detection', cv.WINDOW_NORMAL)
cv.setWindowProperty('Vein Detection', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
screen_res = int(1920 * 0.7), int(1080 * 0.7)
screen_resOG = int(1920), int(1080)

while True:
    frame = picam2.capture_array()
    frame = cv.normalize(frame, None, alpha=25, beta=0.8*255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

    # Convert the image to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Apply morphological opening
    kernel = np.ones((5,5),np.uint8)
    opening = cv.morphologyEx(blurred, cv.MORPH_OPEN, kernel)

    bilateral = cv.bilateralFilter(opening, 9, 75, 75)

    # Apply adaptive thresholding
    blockSize = 15  # adjust this value
    C = 2  # adjust this value
    edges = cv.adaptiveThreshold(bilateral, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, blockSize, C)

    # Apply morphological closing
    closing = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)

    # Create a color mask
    color_mask = np.zeros((closing.shape[0], closing.shape[1], 3), dtype=np.uint8)
    color_mask[closing == 255] = [0, 255, 0]  # BGR format

    color_mask_resized = cv.resize(color_mask, screen_res, interpolation = cv.INTER_LINEAR)
    
    invertedImage = cv.flip(color_mask_resized, -1)
    
    paddedImage = cv.copyMakeBorder(invertedImage, 0, screen_resOG[1] - screen_res[1], 0 , screen_resOG[0] - screen_res[0], cv.BORDER_CONSTANT, value=[0,0,0])

    # Display the resulting frame
    cv.imshow('Vein Detection', paddedImage)
    cv.imshow('Vein Image', gray)

    if cv.waitKey(1) == ord('q'):
        break



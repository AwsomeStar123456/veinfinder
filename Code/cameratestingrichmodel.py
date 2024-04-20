from picamera2 import Picamera2, Preview
from libcamera import controls
import cv2 as cv
import numpy as np
import config
import torch
from PIL import Image
import time
import os
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL, x=50, y=100, width=640, height=480)
picam2.start()
picam2.set_controls({"ExposureTime": 50000, "AnalogueGain":2.0, "Contrast": 2.0, "AeEnable": False, "AwbEnable": False})

model = "/home/intelengineers/Semrah/unet.pth.tar" # Initialize your model here
checkpoint_path = "/home/intelengineers/Semrah/unet.pth.tar" # Path to your model checkpoint

for i in range(12):
    time.sleep(100)
    frame = picam2.capture_file("ModelInput.jpg")
    cv.imshow('Live Feed', frame)
    generate_model_prediction(model, checkpoint_path, "ModelInput" + ".jpg", "ModelOutput")

cv.destroyAllWindows()
picam2.stop()

def generate_model_prediction(
        model, checkpoint_path, image_path, output_path, resize=1.):
    '''
    Save the predictions of a model on an image to a file

    Parameters:
    ----------
    model: torch.nn.Module
        Model to use for prediction
    checkpoint_path: str
        Path to the model checkpoint file
    image_path: str
        Path to the image file
    output_path: str
        Path to save the predictions to
    resize: float | tuple, Default: 1 (no resize)
        The size to resize the image to before predicting.
        This should match the size the model was trained on
            If a float, the image is resized by the factor
            If a tuple, the image is resized to the specified size
    '''

    # Load the model from the specified path
    # optimizer is not needed for prediction
    load_checkpoint(model, None, checkpoint_path)
    # Load and preprocess the image
    image = Image.open(image_path)
    # check if resize is a float
    if isinstance(resize, float):
        image = image.resize(
            (int(image.width * resize),
             int(image.height * resize)))
    elif isinstance(resize, tuple):
        image = image.resize(resize)
    else:
        try:
            resize = float(resize)
            image = image.resize(
                (int(image.width * resize),
                 int(image.height * resize)))
        except:
            raise ValueError(
                "resize must be a float or a tuple of two integers")

    # Normalize and add batch dimension
    image_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    # Predict
    model.eval()
    with torch.no_grad():
        y_fake = model(torch.tensor(image_array, dtype=torch.float32))
        # Normalize y_fake from [0, 255] to [0, 1] for matplotlib
        y_fake = y_fake / 255.0
        suffix = output_path.split('.')[-1]
        # Save the predictions to a file
        if suffix == 'npy':
            np.save(output_path, y_fake.numpy())
        elif suffix in ['.jpg', '.jpeg', '.png']:
            # Convert to uint8 and save as an image
            Image.fromarray(y_fake.numpy()).save(output_path)

def load_checkpoint(model, optimizer, filename):
    print("=> Loading checkpoint")
    checkpoint = torch.load(filename, map_location=config.DEVICE)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])

# for i in range(12):
# 	time.sleep(100)
# 	picam2.capture_file("Ajla" + str(i) + ".jpg")

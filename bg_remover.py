from rembg import remove
from PIL import Image
import numpy as np
import cv2
import io

def remove_background(input_image_path, output_image_path):
    # Open the input image file
    with open(input_image_path, 'rb') as file:
        input_image_data = file.read()

    # Use rembg to remove the background
    output_image_data = remove(input_image_data)

    # Convert raw bytes back to an image
    output_image = Image.open(io.BytesIO(output_image_data))

    # Save the output image
    output_image.save(output_image_path, 'PNG')

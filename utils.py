# utils.py

from PIL import Image
import os

def validate_image_extension(filename):
    """
    Check if the file is a valid image with jpg or png extension.
    """
    valid_extensions = ['.jpg', '.jpeg', '.png']
    return os.path.splitext(filename)[1].lower() in valid_extensions

def load_image(image_path):
    """
    Load an image from the given path.
    """
    try:
        return Image.open(image_path)
    except IOError as e:
        raise IOError(f"Unable to load image. Make sure the file exists and is an image file. Error: {e}")

def save_image(image, output_path):
    """
    Save the image to the given path.
    """
    try:
        image.save(output_path, 'PNG')
    except IOError as e:
        raise IOError(f"Unable to save image. Error: {e}")

def is_file_path_valid(file_path):
    """
    Check if the provided file path is valid.
    """
    return os.path.isfile(file_path) and validate_image_extension(file_path)

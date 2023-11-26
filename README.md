# Background Remover

This Python program removes the background from images in JPG or PNG format using the `rembg` library.

## Installation

Before running the program, you need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

This will install the following Python packages as specified in `requirements.txt`:

- opencv-python-headless
- numpy
- pillow
- rembg

## Usage

To use the program, run `main.py` with the input image path and the desired output image path as arguments:

```bash
python main.py <input_image_path> <output_image_path>
```

For example:

```bash
python main.py input.jpg output.png
```

The program will then process the image and save a new image with the background removed to the specified output path.

## Files

- `requirements.txt`: A list of Python packages required to run the program.
- `main.py`: The main script that you run to remove the background from an image.
- `bg_remover.py`: Contains the function `remove_background` which uses the `rembg` library to remove the background from the image.
- `utils.py`: Helper functions for validating image extensions and handling image loading and saving.
- `README.md`: This file, which provides documentation for the project.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Notes

- The program currently supports `.jpg`, `.jpeg`, and `.png` image formats.
- The output image will be saved in PNG format to preserve the transparency of the background.

## License

This project is open-sourced and free to use. Please refer to the LICENSE file for more details.

## Contributions

Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## Acknowledgments

This project utilizes the `rembg` library for background removal. Kudos to the developers of `rembg` for their fantastic work.


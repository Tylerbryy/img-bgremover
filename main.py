import sys
from bg_remover import remove_background
from utils import save_image


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_name = input("Enter the output image file name (it will be saved in the root folder): ")
    output_image_path = f"{output_image_name}.png"  # Append the .png extension

    remove_background(input_image_path, output_image_path)
    print(f"Background removed successfully. Check the output at {output_image_path}")

if __name__ == "__main__":
    main()

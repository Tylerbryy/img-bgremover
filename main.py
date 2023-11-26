import sys
from bg_remover import remove_background

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    try:
        remove_background(input_image_path, output_image_path)
        print(f"Background removed successfully. Check the output at {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

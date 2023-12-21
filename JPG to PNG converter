from PIL import Image
import os
import sys


def jpg_to_png(input_path, output_path):
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Convert and save as PNG
            img.save(output_path, 'PNG')
            print(f"Conversion successful. Image saved as {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def batch_convert(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all JPEG files in the input folder
    jpg_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]

    # Convert each JPEG file to PNG
    for jpg_file in jpg_files:
        jpg_path = os.path.join(input_folder, jpg_file)
        png_file = os.path.splitext(jpg_file)[0] + '.png'
        png_path = os.path.join(output_folder, png_file)
        jpg_to_png(jpg_path, png_path)

if __name__ == "__main__":
    # Specify the input and output folder paths
    input_folder = os.path.join(sys.argv[1])
    output_folder = os.path.join(sys.argv[2])

    # Call the batch conversion function
    batch_convert(input_folder, output_folder)

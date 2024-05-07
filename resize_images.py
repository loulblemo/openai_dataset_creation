import sys
import os

from PIL import Image

def resize_images(input_folder, output_folder, target_size=(512, 512)):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                img = Image.open(input_path)
                img_resized = img.resize(target_size, Image.ANTIALIAS)
                img_resized.save(output_path)
                print("Resized" + filename + " to " + str(target_size))
            except Exception as e:
                print("Error processing" + filename + ": " + str(e))


if __name__ == "__main__":
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    target_size = (512, 512)  # Change to your desired size

    resize_images(input_folder, output_folder, target_size)

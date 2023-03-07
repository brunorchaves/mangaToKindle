from PIL import Image
import os
import glob

# Define the directory path
directory_path = 'imgTest/'

# Define the compression level
quality = 20

# Loop through all image files in the directory
for file_path in glob.glob(os.path.join(directory_path, '*.jpg')):
    # Open the image using Pillow
    image = Image.open(file_path)

    # Save the compressed image
    image.save(file_path, optimize=True, quality=quality)

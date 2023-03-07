import cv2
import os
import numpy as np
from PIL import Image

# Load the image
img = cv2.imread("082_02.jpg")
input_size = os.path.getsize("082_02.jpg") / (1024 * 1024)
print("Input image size: {:.2f} MB".format(input_size))
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow("Grayscale Image", gray_img)

# Define the image path
image_path = '082_02.jpg'

# Open the image using Pillow
image = Image.open(image_path)

# Define the compression level
quality = 20

# Save the compressed image
image.save('compressed_image.jpg', optimize=True, quality=quality)

# Display the grayscale image
cv2.imshow("compressed_image", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
output_size = os.path.getsize("compressed_image.jpg") / (1024 * 1024)
print("output image size: {:.2f} MB".format(output_size))

# TODO
# - extract files from multiples folders done
# - use open cv to sharp images
# - compress sharpened images
# https://stackoverflow.com/questions/58792626/extract-all-files-from-multiple-folders-with-python
# Naruto donwload
# https://www.dattebane.com/pagina/Naruto%20Mangas?fb_comment_id=585511374895338_639233669523108 

import os
from fpdf import FPDF
import rarfile
import os, zipfile
import re


output_dir = 'img/'
source_dir = output_dir


#creates a list of all directories names
def get_directory_names(directory_path):
    # Initialize an empty list to hold directory names
    directory_names = []
    
    # Get a list of all files and directories in the given directory
    items = os.listdir(directory_path)
    
    # Iterate over each item in the directory
    for item in items:
        # Check if the item is a directory
        if os.path.isdir(os.path.join(directory_path, item)):
            # If it is a directory, add its name to the list
            directory_names.append(item)
    
    return directory_names

directory_path = source_dir
directory_names = get_directory_names(directory_path)

# numberOfDirs = (len(directory_names))
# print(numberOfDirs)

for dirIter in directory_names:
    #2 change the files names 
    folder = source_dir+dirIter+"/"
    # print(folder)
    count = 1

    pathName = os.path.dirname(folder)
    folderName = str(os.path.basename(pathName))
    # print(folderName)
    mangaNumber = ""
    for c in folderName:
        if c.isdigit():
            mangaNumber = mangaNumber + c
    # print(mangaNumber)
    # iterate all files from a directory
    for file_name in os.listdir(folder):
        
        # Construct old file name
        source = folder + file_name

        # Adding the count to the new file name and extension
        destination = folder + mangaNumber +"_"+ file_name

        # Renaming the file
        os.rename(source, destination)
        count += 1
    # print('All Files Renamed')

import shutil

folder = source_dir
subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

for sub in subfolders:
    for f in os.listdir(sub):
        src = os.path.join(sub, f)
        dst = os.path.join(folder, f)
        shutil.move(src, dst)


# 3 create the pdf

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)
import glob
from PIL import Image
import os
# Define the directory path
directory_path = 'img/'

# Define the compression level
quality = 20

# Loop through all image files in the directory
for file_path in glob.glob(os.path.join(directory_path, '*.jpg')):
    # Open the image using Pillow
    newimage = Image.open(file_path)

    # Save the compressed image
    newimage.save(file_path, optimize=True, quality=quality)



# Define the input and output file paths
input_file_path = 'input.jpg'
output_file_path = 'output.jpg'

# Open the input image file


pdf = FPDF()
pdf.set_auto_page_break(0)

imagelist = [i for i in os.listdir(source_dir) if i.endswith('jpg')]
# imagelist is the list with all image filenames
for image in sorted(imagelist):

    pdf.add_page()
    pdf.image(output_dir + image, w=190, h=280)

mangaName = input("Write the name of the manga: \n")
pdf.output(mangaName +".pdf", "F")

# import PyPDF2

# # Define the input and output file paths
# input_file_path = "'"+"pdfs/"+mangaName+ ".pdf" + "'"
# output_file_path = 'img/'

# # Open the input PDF file
# with open(input_file_path, 'rb') as input_file:
#     # Create a PDF reader object
#     pdf_reader = PyPDF2.PdfFileReader(input_file)

#     # Create a PDF writer object
#     pdf_writer = PyPDF2.PdfFileWriter()

#     # Loop through each page of the PDF
#     for page_num in range(pdf_reader.getNumPages()):
#         # Get the current page
#         page = pdf_reader.getPage(page_num)

#         # Compress the page
#         page.compressContentStreams()

#         # Add the compressed page to the PDF writer object
#         pdf_writer.addPage(page)

#     # Open the output PDF file
#     with open(output_file_path, 'wb') as output_file:
#         # Write the output PDF file
#         pdf_writer.write(output_file)

# # Remove the input file
# # os.remove(input_file_path)





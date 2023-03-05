# TODO
# - extract files from multiples folders 
# https://stackoverflow.com/questions/58792626/extract-all-files-from-multiple-folders-with-python

import os
from fpdf import FPDF
import rarfile
import os, zipfile

output_dir = 'img/'
source_dir = 'img/'

# os.chdir(dir_name) # change directory from working dir to dir with files

# Get a list of all .rar files in the directory
rar_files = [file for file in os.listdir(source_dir) if file.endswith(".rar")]

# Extract each .rar file in the directory
for rar_file in rar_files:
    # Open the .rar file
    with rarfile.RarFile(os.path.join(source_dir, rar_file)) as rf:
        # Extract all files in the .rar file to the current directory
        rf.extractall(source_dir)

# pdf = FPDF()
# pdf.set_auto_page_break(0)

# imagelist = [i for i in os.listdir(source_dir) if i.endswith('jpg')]
# # imagelist is the list with all image filenames
# for image in sorted(imagelist):
#     pdf.add_page()
#     pdf.image(output_dir + image, w=190, h=280)

# pdf.output("naruto.pdf", "F")




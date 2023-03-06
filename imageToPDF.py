# TODO
# - extract files from multiples folders 
# https://stackoverflow.com/questions/58792626/extract-all-files-from-multiple-folders-with-python

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


pdf = FPDF()
pdf.set_auto_page_break(0)

imagelist = [i for i in os.listdir(source_dir) if i.endswith('jpg')]
# imagelist is the list with all image filenames
for image in sorted(imagelist):
    pdf.add_page()
    pdf.image(output_dir + image, w=190, h=280)

pdf.output("narutoVol9.pdf", "F")




  
import os
import csv

def get_file_names(folderpath, out="output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    files = os.listdir(folderpath)
    with open(out, 'w') as output_file:
        for file in files:
            output_file.write(file + '\n')

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file_name in file_names:
        with open(file_name, "r") as f:
            for line in f:
                    print(line)
                    break

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file_name in file_names:
        with open(file_name, "r") as f:
            for line in f:
                print(line)
                break

# def write_headlines(md_files, out=output.txt):
#     """takes a list of md files and writes all headlines (lines starting with #) to a file"""
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program for reading from and writing to files')
    parser.add_argument('path', help='The path of the cvs file')
    parser.add_argument('-f', '--file_name', help='The name of the file')

    args = parser.parse_args()
    
    print('Path:', args.path)
    print('File: ', args.file_name)

import csv

#filename = 'enrollment_forecast.csv'
filename = args.path

def print_file_content(file):
    
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)
        
        for row in reader:
            print(str(reader.line_num) + ' ' + str(row))

            if reader.line_num > 10:
                break    
        
print_file_content(filename)

import platform

my_list = [("ek", "1", "comment"), ("ek2", "2", "some comment"), ("ek3", "3", "some comment")]
output_file = 'output.csv'

def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
    
        for element in lst:
            output_writer.writerow([element[0], element[1], element[2]])
            
write_list_to_file(output_file, my_list)

a_list = []

filename = 'enrollment_forecast.csv'

def read_csv(input_file):

    with open(input_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            a_list.append(row)
        
    print(a_list)

read_csv(filename)
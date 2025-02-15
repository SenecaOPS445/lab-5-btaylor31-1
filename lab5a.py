#!/usr/bin/env python3
# Author ID: btaylor31

def read_file_string(file_name):
    # Takes file_name as a string for a file name return string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    # Takes a file_name as string for a name 
    # returns its entire contents as a list of lines
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
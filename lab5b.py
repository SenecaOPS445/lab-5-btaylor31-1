#!/usr/bin/env python3
# Author ID: btaylor31

def add(a, b):
    try:
        # Inputs converted to integers
        a = int(a)
        b = int(b)
        return a + b
    except ValueError:
        return 'error: could not add numbers'


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return 'error: could not read file'


def read_file_string(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()  
    except FileNotFoundError:
        return 'error: could not read file'


def read_file_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        return 'error: could not read file'

def append_file_string(filename, string_to_append):
    try:
        with open(filename, 'a') as file:
            file.write(string_to_append)  # Append 
    except FileNotFoundError:
        return 'error: could not write to file'

def write_file_list(filename, list_to_write):
    try:
        with open(filename, 'w') as file:  # File is opened in write mode
            for item in list_to_write:
                file.write(item + '\n')  # Add new line to each item with write function
    except FileNotFoundError:
        return 'error: could not write to file'

def copy_file_add_line_numbers(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            with open(output_filename, 'w') as outfile:
                line_number = 1
                for line in infile:
                    outfile.write(f"{line_number}:{line.strip()}\n")
                    line_number += 1
    except FileNotFoundError:
        return 'error: could not read or write file'
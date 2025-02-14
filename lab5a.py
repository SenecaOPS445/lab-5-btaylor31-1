#!/usr/bin/env python3
# Author ID:  btaylor31

def read_file_string(file_name):
    """Reads the entire content of a file and returns it as a string."""
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: {file_name} not found."
    except Exception as e:
        return f"Error: {str(e)}"

def read_file_list(file_name):
    """Reads the file and returns its contents as a list of lines without newline characters."""
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return [f"Error: {file_name} not found."]
    except Exception as e:
        return [f"Error: {str(e)}"]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
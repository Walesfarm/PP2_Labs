import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = "A.txt"
line_count = count_lines_in_file(file_path)
print("Number of lines in the file:", line_count)
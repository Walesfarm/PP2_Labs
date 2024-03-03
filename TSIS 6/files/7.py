import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

source_file = "A.txt"
destination_file = "B.txt"
copy_file_contents(source_file, destination_file)
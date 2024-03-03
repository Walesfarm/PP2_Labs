import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def write_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(str(item) + '\n')

file_path = "A.txt"
my_list = [1, 2, 3, 4, 5]
write_list_to_file(file_path, my_list)
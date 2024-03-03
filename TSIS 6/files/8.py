import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

def delete_file_by_path(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")


file_to_delete = "Z.txt"
delete_file_by_path(file_to_delete)
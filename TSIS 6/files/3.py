import os

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")
def get_filename_and_directory(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "Path does not exist", None

filename, directory = get_filename_and_directory(path)
print("Filename:", filename)
print("Directory:", directory)
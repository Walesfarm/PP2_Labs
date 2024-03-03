import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_directories_files = [os.path.join(path, item) for item in os.listdir(path)]
    return directories, files, all_directories_files

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")
directories, files, all_items = list_directories_files(path)
print("Directories:", directories)
print("Files:", files)
print("All Directories and Files:", all_items)
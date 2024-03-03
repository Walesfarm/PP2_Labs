import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")
exists, readable, writable, executable = check_path_access(path)
print("Exists:", exists)
print("Readable:", readable)
print("Writable:", writable)
print("Executable:", executable)
import os
import string

home = os.path.expanduser("~")
path = os.path.join(home, "Documents")

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        pass  # File created with no content
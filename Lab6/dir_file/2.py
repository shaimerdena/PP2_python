# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

def access(file_path):
    if os.access(file_path, os.F_OK):
        print("The path exists.")
    else:
        print("The path doesn't exist.")
    if os.access(file_path, os.R_OK):
        print("Readable.")
    else:
        print("Not readable.")
    if os.access(file_path, os.W_OK):
        print('Writable.')
    else:
        print('Not writable.')
    if os.access(file_path, os.X_OK):
        print('Executable.')
    else:
        print('Not executable.')
    
path = r"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab6\directory"
path0 = r"C:\Users\Shaim\OneDrive\Рабочий стол\AYYYau"
access(path)
print()
access(path0)


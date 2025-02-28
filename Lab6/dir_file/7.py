# Write a Python program to copy the contents of a file to another file

def copying(file_path1, file_path2):
    f1 = open(file_path1)
    reading = f1.read()
    f2 = open(file_path2, "w")
    for line in reading:
        f2.write(line)
    f1.close()
    f2.close()

path1 = r"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab6\directory\Ayau.txt"
path2 = r"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab6\directory\Copy.txt"
copying(path1, path2)

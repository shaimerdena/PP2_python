import os


def control(file_path, string):
    print(os.listdir(os.path.dirname(file_path)))
    if os.access(file_path, os.R_OK):
        print("Readable")
    if os.access(file_path, os.R_OK):
        print("Writable")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(string)


path = r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\practicing\regex\row.txt'
str = input('Input a string: ')
control(path, str)
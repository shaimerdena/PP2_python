# Write a Python program to write a list to a file.

def writing(file_path, list_name):
    with open(file_path, "a") as f:

        for item in list_name:
            f.write(f'{item} ')

list_ex = ['I', 'have', 'a', 'cat']

path = r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab6\directory\Ayau.txt'

writing(path, list_ex)

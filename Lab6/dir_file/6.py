# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

def generating():
    for i in range(65, 91):
        l = open(rf"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab6\result\{chr(i)}.txt", "a")

generating()
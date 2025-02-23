import re

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

print("6)", end = " ")
with open("example1", "r") as file:
    data = file.read()
    print(re.sub(r"[ ,.]", ":", data))

#Write a python program to convert snake case string to camel case string.

print("7)", end = " ")
with open("example1", "r") as file:
    data = file.read().strip()
    x = re.split("_", data)
    camel_case = x[0] + "".join(word.capitalize() for word in x[1:])
    print(camel_case)

#Write a Python program to split a string at uppercase letters.

print("8)", end = " ")
with open("example1", "r") as file:
    data = file.read()
    x = re.split(r"(?=[A-Z])", data)
    print(x)

#Write a Python program to insert spaces between words starting with capital letters.

print("9)", end = " ")
with open("example1", "r") as file:
    data = file.read()
    x = re.sub(r"([a-z])([A-Z])", r"\1 \2", data)
    print(x)

#Write a Python program to convert a given camel case string to snake case.

print("10)", end = " ")
with open("example1", "r") as file:
    data = file.read().strip()
    x = re.sub(r"([a-z])([A-Z])", r"\1 \2", data)
    x = re.split(" ", x)
    snake_case = "_".join(word.lower() for word in x)
    print(snake_case)
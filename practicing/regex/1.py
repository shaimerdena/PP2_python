import re
with open(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab5\row.txt', encoding="utf-8") as hand:
    text = hand.read()
x = re.findall(r"^Д*", text, re.MULTILINE)

if x:
    print("girrll")
    for i in x:
        print(x)
else:
    print("boyyy")
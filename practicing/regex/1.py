import re
with open(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\practicing\regex\row.txt', "r", encoding="utf-8") as hand:
    text = hand.read()
    print(re.findall(r"[0-9].+", text))
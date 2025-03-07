import re
with open(r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\practicing\regex\row.txt', "r", encoding="utf-8") as hand:
    text = hand.read()
    print(re.sub("0", '1', text))
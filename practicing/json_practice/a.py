import json


with open("practice_data.json", "r", encoding = "utf-8") as file:
    data = json.load(file)
    
for student in data["students"]:
    print(f"Student name: {student['name']}, age: {student['age']}")
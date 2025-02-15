import os
import json

os.chdir("C:/Users/Shaim/OneDrive/Рабочий стол/Python/Lab4/json_files")

with open('sample_data.json', 'r') as json_file:
    a = json.load(json_file)

print("Interface Status")
print("="*94)
print(f"{'DN':<52} {'Description':<25} {'Speed':<10} {'MTU':<6}")
print("-" * 50, " ", "-" * 20, " ", "-" * 10, " ", "-" * 6)

for item in a["imdata"]: 
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes["mtu"]
    print(f"{dn:<50} {description:<25} {speed:<12} {mtu:<6}")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")      #packing a tuple

(green, yellow, *red) = fruits    #using asterisk, bc the number of variables is less than the number of values

print(green)
print(yellow)
print(red)    

print("------------------------------------------------")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
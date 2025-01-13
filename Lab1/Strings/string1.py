print("It's alright")  #Quotes Inside Quotes

#multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

a = "Hello, World!"
print(a[1])             #Get the character at position 1

for x in "banana":
  print(x, end = " ")       #Looping Through a String
print()
print(len("banana"))        #the length of a string

txt = "The best things in life are free!"
print("free" in txt)                          #Check String
if "free" in txt:
  print("Yes, 'free' is present.")
if "green" not in txt:
  print("No, 'green' isn't present.")

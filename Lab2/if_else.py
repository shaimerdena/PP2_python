a = 200
b = 33
c = 60

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#short hand: Ternary Operators, or Conditional Expressions.
#short hand if
if a > b: print("a is greater than b")

#short hand if else
print("A") if a > b else print("B")

#short hand if elif else
print("A") if a > b else print("=") if a == b else print("B")



#and
if a > b and c > a:
  print("Both conditions are True")

#or
if a > b or a > c:
  print("At least one of the conditions is True")

#not
if not a > b:
  print("a is NOT greater than b")

#nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#the pass statement
a = 33
b = 200
if b > a:
  pass
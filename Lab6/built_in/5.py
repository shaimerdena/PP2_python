# Write a Python program with builtin function that returns True if all elements of the tuple are true.

def check(tuple):
    return all(tuple)

tuple1 = (True, False, 1, 0)
tuple2 = (1, True, [1,2,3], (1,2,3), 'Ayau')
print(check(tuple1))
print(check(tuple2))
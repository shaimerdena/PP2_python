# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.




#union method = "|" method: these methods are the same         (union: will exclude any duplicate items.)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2             #joins sets with sets
print(set3)

#joining multiple set using the union method and "|" method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2 | set3 |set4
print(myset)

#joining a set and a tuple using union method (we can't use "|" method)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#update method: The update() changes the original set, and does not return a new set.       (will exclude any duplicate items.)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection method and "&" method (will return a new set, that only contains the items that are present in both sets.)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2             #joins sets with sets
print(set3)

#intersection_update() method (will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

#####The values True and 1 are considered the same value. The same goes for False and 0.

#difference method and "-" method (will return a new set that will contain only the items from the first set that are not present in the other set.)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2         #joins set with sets
print(set3)

#difference_update() method (will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

#Symmetric difference and "^" method (will keep only the elements that are NOT present in both sets.)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2            #joins sets with sets
print(set3)

#symmetric_difference_update() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)
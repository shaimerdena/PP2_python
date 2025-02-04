from itertools import permutations

def permutation(str):
    perm_list = permutations(str)
    for i in perm_list:
        print("".join(i))

str = input()
permutation(str)
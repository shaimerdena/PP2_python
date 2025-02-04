def sort(list):
    res = []
    for i in list:
        if res.count(i) == 0:
            res.append(i)
    for i in res:
        print(i, end = " ")

list = input().split()
for i in list:
    i = int(i)
sort(list)
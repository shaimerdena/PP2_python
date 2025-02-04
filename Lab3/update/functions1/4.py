def filter(nums):
    for i in nums:
        count = 0
        for j in range(2, i):
            if i%j == 0:
                count += 1
        if count == 0 and i!=1 and i!=0:
            print(i, end = " ")
    print()

list = input().split()
for i in range(len(list)):
    list[i] = int(list[i])
filter(list)

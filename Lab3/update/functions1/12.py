def histogram(list):
    for i in list:
        for j in range(int(i)):
            print("*", end = "")
        print()

list = input().split()
histogram(list)
def reverse(list):
    for i in range(len(list)-1, -1, -1):
        print(list[i], end = " ")

sentence = input().split()
reverse(sentence)
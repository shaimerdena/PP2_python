def palindrome(word):
    reversed = word[::-1]
    if word == reversed:
        return True
    return False

word = input()
print(palindrome(word))
from random import randint

def guess():
    name = input("Hello! What is your name?\n")
    print("Well,", name + ", I am thinking of a number between 1 and 20.")

    num = randint(1, 20)
    count = 0

    while True:
        inp = int(input("Take a guess.\n"))
        count += 1
        if inp == num:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
        else:
            if inp > num:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
    
guess()
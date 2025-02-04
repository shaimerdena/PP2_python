def solve(numheads, numlegs):
    chicken = 0
    while True:
        if (2*chicken + 4*(numheads - chicken) == numlegs):
            print(f"number of chickens: {chicken}")
            print("number of rabbits:", numheads - chicken)
            break
        chicken += 1

solve(36, 94)
class Prime:
    def __init__(self, nums):
        self.nums = nums

    def primes(self, num):
        count = 0
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False
        
    def filtering(self):
        return list(filter(lambda x: self.primes(x), self.nums))
    

l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
primes = Prime(l)
print(primes.filtering())
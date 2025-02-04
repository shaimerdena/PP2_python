def spy_game(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            res.append(nums[i])
    for i in range(len(res)-2):
        if res[i] ==0 and res[i+1] == 0 and res[i+2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 
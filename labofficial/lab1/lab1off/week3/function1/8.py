def spy_game(nums):
    for x in range(len(nums) - 2):
        if nums[x+1] == nums[x] == 0 and nums[x+2] == 7:
            return True
    return False
            
    

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

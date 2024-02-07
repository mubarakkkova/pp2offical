def has_33(nums):
    for x in range(len(nums) - 1):
        if nums[x+1] == nums[x] == 3:
            return True
    return False
            
    

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if(diff in seen):
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
    return seen


var1 = twoSum([2, 3, 4, 5, 7, 8, 9], 10)
print(var1)

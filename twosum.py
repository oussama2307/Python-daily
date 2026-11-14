def TwoSum(nums,target):
    indexes = {}
    for i in range(0,len(nums)):
        dif = target - nums[i]
        if dif in indexes:
            indexes[dif].append(i)
            return indexes[dif]
        else:
            indexes[nums[i]] = [i]

nums = [4,5,6]
target = 10
print(TwoSum(nums,target))
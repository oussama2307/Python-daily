def topKFrequent(nums,k):
    frequency = {}
    for i in nums:
        frequency[i] = frequency.get(i,0)+1
    result = [key for key,v in frequency.items() if v>= k]
    return result
topKFrequent

nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent(nums,2))
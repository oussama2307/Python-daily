def topKFrequent(nums,k):
    frequency = {}
    for i in nums:
        frequency[i] = frequency.get(i,0)+1
    result = sorted(frequency,key = frequency.get,reverse=True)
    
    return result               

def topkFrequent(nums,k):
    frequency = {}
    for i in nums:
        frequency[i] = frequency.get(i,0)+1
    frequecies = [[] for _ in range(len(nums))]
    for key , value in frequency.items():
        frequecies[value].append(key)
    result = []
    for i in range(len(nums)-1,0,-1):
        if k == 0:
            return result
        if len(frequecies[i]) != 0:
            result += frequecies[i]
            k -= len(frequecies[i])


nums = [1,2,2,3,3,5,5,5,6,6,6,6,6,7,3]
k = 2
##print(topKFrequent(nums,k))
print(topkFrequent(nums,k))

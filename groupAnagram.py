def groupAnagram(strs):
    groupes = {}
    
    for str in strs:
        position = [0] * 26
        for letter in str:
            number = ord(letter.lower()) - ord("a")
            position[number] += 1
            tupleposition = tuple(position)
        if tupleposition in groupes:
            groupes[tupleposition].append(str)
        else:
            groupes[tupleposition] = [str]
    return list(groupes.values())
        
strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagram(strs))

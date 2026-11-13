def isAnagram(s,t) :
    lettersS = {}
    lettersT = {}
    for i in s:
        lettersS[i] = lettersS.get(i,0)+1
    for i in t:
        lettersT[i] = lettersT.get(i,0)+1
    if lettersS == lettersT :
        return True
    return False

s = "racecar"
t = "carrace"

print(isAnagram(s,t))
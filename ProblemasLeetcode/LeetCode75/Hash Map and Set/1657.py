def closeStrings(word1: str, word2: str) -> bool:
    ocurr1 = {}
    ocurr2 = {}
    for w in word1:
        if w in ocurr1:
            ocurr1[w]+=1
        else:
            ocurr1[w]=1
    for w in word2:
        if w in ocurr2:
            ocurr2[w]+=1
        else:
            ocurr2[w]=1
    if set(word1)==set(word2) and sorted(ocurr1.values())==sorted(ocurr2.values()):
        return True
    else:
        return False

print(closeStrings(word1 = "abc", word2 = "bca"))
print(closeStrings(word1 = "a", word2 = "aa"))
print(closeStrings(word1 = "cabbba", word2 = "abbccc"))
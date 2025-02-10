def mergeAlternately(self, word1: str, word2: str) -> str:
    res = ""
    t1,t2=len(word1),len(word2)
    for i in range(min(t1,t2)):
        res+=word1[i]+word2[i]
    if t1<t2:
        res+=word2[t1:]
    elif t1>t2:
        res+=word1[t2:]
    return res
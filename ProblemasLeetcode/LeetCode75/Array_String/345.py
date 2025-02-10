def reverseVowels(self, s: str) -> str:
    myvowels=[]
    vowels = {"a","e","i","o","u","A","E","I","O","U"}
    res = ""
    for c in s:
        if c in vowels:
            myvowels.append(c)
    for c in s:
        if c in vowels:
            res+=myvowels.pop()
        else:
            res+=c
    return res
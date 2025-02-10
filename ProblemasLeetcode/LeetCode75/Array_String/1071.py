def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str1==str2:
        return str1
    res = ""
    n1 = len(str1)
    n2 = len(str2)
    mini, maxi = min(n1,n2), max(n1,n2)
    for i in range(mini):
        aux = str1[:i+1]
        t1, t2 = False, False
        j=1
        while j*len(aux)<=maxi:
            if str1==aux*j:
                t1=True
            elif str2==aux*j:
                t2=True
            j+=1
        if t1 and t2:
            res = aux
    return res

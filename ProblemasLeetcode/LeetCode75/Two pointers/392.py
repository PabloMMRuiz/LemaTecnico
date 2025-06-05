def isSubsequence(s: str, t: str) -> bool:
        if len(s)>len(t):return False
        if len(s)==0:return True
        subsequence=0
        for i in range(0,len(t)):
            if s[subsequence] == t[i]:
                subsequence+=1
            if subsequence == len(s):
                return True
        return False

ss = "acfe"
tt = "abcdfeddd"
print(isSubsequence(ss,tt))



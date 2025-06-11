def removeStars(s: str) -> str:
    res = []
    for c in s:
        if c=="*":
            res.pop()
        else:
            res.append(c)
    return "".join(res)

print(removeStars("leet**cod*e"))
print(removeStars("erase*****"))
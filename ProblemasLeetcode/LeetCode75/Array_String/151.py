def reverseWords(s: str) -> str:
    res = ""
    words = []
    current = ""
    for c in s:
        if c != " ":
            current += c
        elif current != "":
            words.append(current)
            current = ""
    if current != "":
        words.append(current)
    for i in range(len(words)-1,-1,-1):
        res += words[i] + " "
    return res[:-1]

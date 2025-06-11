def decodeString(s):
    stack = []
    curStr = ""
    curNum = 0
    for c in s:
        if c == "[":
            stack.append(curStr)
            stack.append(curNum)
            curStr = ""
            curNum = 0
        elif c == "]":
            num = stack.pop()
            prevStr = stack.pop()
            curStr = prevStr + curStr*num
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curStr += c
    return curStr
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = deque()
        dir = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                dir.append(i)
        while rad and dir:
            if rad.popleft() < dir.popleft():
                rad.append(n)
            else:
                dir.append(n)
            n += 1
        if rad:
            return "Radiant"
        else:
            return "Dire"


        
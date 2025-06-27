from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        seen = set()
        for i in range(len(isConnected)):
            if i not in seen:
                provinces += 1
                stack = [i]
                while stack:
                    city = stack.pop()
                    seen.add(city)
                    neigh = isConnected[city]
                    for j in range(len(neigh)):
                        if neigh[j] == 1 and j not in seen:
                            stack.append(j)
        return provinces

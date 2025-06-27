from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = rooms[0][:]
        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                stack.extend(rooms[room])
        
        return len(visited) == len(rooms)

            


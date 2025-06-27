from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(*entrance, 0)])  # queue holds (x, y, distance)
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'  # mark entrance as visited

        while q:
            x, y, d = q.popleft()
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and [x, y] != entrance:
                return d
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'  # mark as visited
                    q.append((nx, ny, d + 1))
        return -1  # no exit found

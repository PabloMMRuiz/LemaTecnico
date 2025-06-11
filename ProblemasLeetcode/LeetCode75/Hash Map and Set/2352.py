def equalPairs(grid) -> int:
    aux = {}
    res = 0
    n = len(grid)
    for row in grid:
        row = tuple(row)
        aux[row] = aux.get(row, 0) + 1

    for j in range(n):
        currentC = tuple([grid[k][j] for k in range(n)])
        res += aux.get(currentC, 0)

    return res

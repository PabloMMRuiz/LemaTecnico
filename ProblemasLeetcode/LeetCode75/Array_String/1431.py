def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    maxi = max(candies)
    res = [c+extraCandies>=maxi for c in candies]
    return res

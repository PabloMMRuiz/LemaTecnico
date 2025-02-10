def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    can = 0
    m = len(flowerbed)
    if m > 1:
        for i in range(m):
            if i == 0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    can+=1
                    flowerbed[i]=1
            elif i == m-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    can+=1
                    flowerbed[i]=1
            else:
                if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                    can+=1
                    flowerbed[i]=1
    else:
        if n == 1 and flowerbed[0]==0:
            return True
        elif n == 0:
            return True
        else:
            return False
    if can >= n:
        return True
    else:
        return False

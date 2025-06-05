def maxArea(height):
    max = 0
    i1 = 0
    i2 = len(height)-1
    while i1<i2:
        area = (i2 - i1)*min(height[i1], height[i2])
        if area > max:
            max = area
        if height[i1]>=height[i2]:
            i2-=1
        else:
            i1+=1
    return max

print(maxArea([1,8,6,2,5,4,8,3,7]))


def moveZeroes(nums) -> None:
    if (len(nums)>1):
        n = len(nums)
        i1 = 0
        i2 = 1
        while i2 < n:
            if nums[i1] == 0 and nums[i2] != 0:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1+=1
                i2+=1
            elif nums[i1] != 0:
                i1+=1
                i2+=1
            elif nums[i1] == 0 and nums[i2] == 0:
                i2+=1

l = [0,1,9,9,0,0,0,2,9,0,3,0]
moveZeroes(l)
print(l)
                
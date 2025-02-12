def increasingTriplet(self, nums: List[int]) -> bool:
    if len(nums)==1 or len(nums)==2:
        return False
    res = False
    if nums[0]<nums[1]:
        min_i = nums[0]
        min_j = nums[1]
    else:
        min_i = nums[0]
        min_j = nums[0]
    for i in range(len(nums)):
        if nums[i]<min_i:
            min_j = min_i
            min_i = nums[i]
        elif nums[i]<min_j and i!=0:
            min_j = nums[i]
        elif nums[i]>min_j and min_i < min_j:
            res = True
    return res
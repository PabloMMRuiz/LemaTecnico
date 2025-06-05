def maxOperations(nums,k):
    nums.sort()
    left = 0
    right = len(nums)-1
    counter = 0

    while left < right:
        if nums[left]+nums[right]==k:
            counter+=1
            left+=1
            right-=1
        elif nums[left]+nums[right]<k:
            left+=1
        elif nums[left]+nums[right]>k:
            right-=1
    return counter
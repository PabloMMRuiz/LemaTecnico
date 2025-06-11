def pivotIndex(nums) -> int:
    prefix_sum = [0]*(len(nums)+1)
    for i in range(len(nums)):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]

    for i in range(len(nums)):
        if prefix_sum[i] == prefix_sum[-1]-prefix_sum[i+1]:
            return i
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))
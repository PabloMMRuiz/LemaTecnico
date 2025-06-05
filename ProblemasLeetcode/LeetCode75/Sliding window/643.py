def findMaxAverage(nums, k):
    max_average = current_average = sum(nums[:k])
    for right in range(k, len(nums)):
        current_average += nums[right] - nums[right-k]
        if current_average > max_average:
            max_average = current_average
    return max_average/k

print(findMaxAverage([7,4,5,8,8,3,9,8,7,6], k = 7))
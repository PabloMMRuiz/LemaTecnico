def longestOnes(nums, k: int) -> int:
    left = max_len = num_zeros = 0
    for right in range(len(nums)):
        if nums[right] == 0: #If the right is a zero, we flip it
            num_zeros += 1
        while num_zeros > k:
            if nums[left] == 0:
                num_zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


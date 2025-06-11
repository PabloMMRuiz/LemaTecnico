def findDifference(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    res = []
    res.append(list(set1.difference(set2)))
    res.append(list(set2.difference(set1)))
    return res
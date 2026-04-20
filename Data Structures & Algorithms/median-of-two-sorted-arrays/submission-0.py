import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        mixed_nums = sorted(nums1 + nums2)
        middle_nums = len(mixed_nums)/2

        print(middle_nums)
        if middle_nums%2 != 0:
            return mixed_nums[int(middle_nums)]
        else:
            return (mixed_nums[int(middle_nums - 1)] + mixed_nums[int(middle_nums)])/2

'''nums1 = [1, 2]
nums2 = [3]
assert Solution().findMedianSortedArrays(nums1, nums2) == 2.0'''
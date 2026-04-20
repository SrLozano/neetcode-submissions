class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        
        return sorted_nums[len(sorted_nums) - k]

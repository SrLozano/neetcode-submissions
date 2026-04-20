class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums: List[int], target: int, l: int, r: int) -> int:
        
        if l > r:
            return -1
        
        m = (l + r) // 2

        if nums[m] == target:
            return m
        elif target > nums[m]:
            return self.binary_search(nums, target, m+1, r)
        else:
            return self.binary_search(nums, target, l, m-1)
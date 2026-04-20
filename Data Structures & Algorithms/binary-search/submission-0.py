class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        mid = len(nums) // 2

        print(f"nums: {nums}, mid: {mid}, target: {target}")

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.search(nums[mid:], target)
        else:
            return self.search(nums[:mid], target)
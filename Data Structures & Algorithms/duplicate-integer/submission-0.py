class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) < 2:
            return False

        hash_map = defaultdict(int)

        for element in nums:
            if hash_map[element] > 0:
                return True

            else:
                hash_map[element] += 1

        return False

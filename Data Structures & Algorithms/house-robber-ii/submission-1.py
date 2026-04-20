class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def dfs(exploring_house, end, mem):
            if exploring_house > end:
                return 0

            if exploring_house in mem:
                return mem[exploring_house]
            
            mem[exploring_house] = max(
                dfs(exploring_house+1, end, mem), 
                nums[exploring_house] + dfs(exploring_house+2, end, mem)
            )
            return mem[exploring_house]

        # Case 1: Exclude the last house
        option1 = dfs(0, len(nums) - 2, defaultdict(int))
        # Case 2: Exclude the first house
        option2 = dfs(1, len(nums) - 1, defaultdict(int))

        return max(option1, option2)
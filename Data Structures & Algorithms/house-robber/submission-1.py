class Solution:
    def rob(self, nums: List[int]) -> int:

        aux_results = defaultdict(int)

        def dfs(exploring_house):
            if exploring_house in aux_results:
                return aux_results[exploring_house]
            
            if exploring_house + 2 in range(len(nums)):
                return max(nums[exploring_house] + dfs(exploring_house + 2), dfs(exploring_house + 1))
            elif exploring_house + 1 in range(len(nums)):
                return max(nums[exploring_house], dfs(exploring_house + 1))
            
            aux_results[exploring_house] = nums[exploring_house]
            return aux_results[exploring_house]

        return dfs(0)
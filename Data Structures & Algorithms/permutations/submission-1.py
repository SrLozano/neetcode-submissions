class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
          
        # base case
        if len(nums) == 1:
            return [[nums[0]]]

        results = []
        for i in range(0, len(nums)):
            copy = nums.copy()
            print(copy)
            aux_num = copy[i]
            copy.pop(i)
            
            permutations = self.permute(copy)

            for permutation in permutations:
                aux_list = [aux_num]
                aux_list.extend(permutation)
                results.append(aux_list)
        
        return results



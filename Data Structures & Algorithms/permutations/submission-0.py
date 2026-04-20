class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive_permute(nums: list[int])-> list[list[int]]:
          
            # base case
            if len(nums) == 1:
                return [[nums[0]]]

            results = []
            for i in range(0, len(nums)):
                copy = nums.copy()
                print(copy)
                aux_num = copy[i]
                copy.pop(i)
                
                permutations = recursive_permute(copy)

                for permutation in permutations:
                    aux_list = [aux_num]
                    aux_list.extend(permutation)
                    results.append(aux_list)
            
            return results


        return recursive_permute(nums)
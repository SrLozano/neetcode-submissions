class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1

        max_capacity = 0

        while l < r:
            
            capacity = min(heights[l], heights[r]) * (r - l)

            if capacity > max_capacity:
                max_capacity = capacity

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

            
        return max_capacity
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # for every number that I have in the possibilities
        for k in range(1, max(piles) + 1):
            h_aux = h

            # can i eat all bananas with the number i?
            for i in range(len(piles)):
                steps_i_need = math.ceil(piles[i]/k)
                h_aux -= steps_i_need
                if h_aux < 0:
                    break 
            
            if h_aux >= 0:
                return k

        
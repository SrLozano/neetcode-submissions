class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0] * len(word1) for _ in range(len(word2))]

    
        for i in range(len(word2)):
            for j in range(len(word1)):
                # base case: starting point in dp cache
                if i == j == 0 and word2[i] != word1[j]:
                    dp[0][0] == 1
                # case same character
                elif word2[i] == word1[j] and i-1>=0 and j-1>=0:
                    dp[i][j] = dp[i-1][j-1]
                # case different character
                else:
                    dp[i][j] = 1 + dp[i-1][j-1]
        
        return dp[len(word2)-1][len(word1)-1]
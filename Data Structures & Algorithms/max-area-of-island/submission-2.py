class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_size = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, island_size):
            grid[i][j] = 0

            for direction in directions:
                mod_i = i + direction[0]
                mod_j = j + direction[1]
                if mod_i in range(len(grid)) and mod_j in range(len(grid[0])):
                    if grid[mod_i][mod_j] == 1:
                        island_size = dfs(mod_i, mod_j, island_size+1)

            return island_size

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_island_size = max(dfs(i, j, 1), max_island_size)
        
        return max_island_size

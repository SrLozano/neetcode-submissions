class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.explore(i, j, grid)
                    num_island+=1
                    print(grid)

        return num_island

    def explore(self, i: int, j:int, grid: List[List[str]]) -> None:
        
        grid[i][j] = '0'

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for direction in directions:
            mod_i, mod_j = i+direction[0], j+direction[1]
            if mod_i >= 0 and mod_i < len(grid) and mod_j >= 0 and mod_j < len(grid[mod_i]):
                if grid[mod_i][mod_j] == '1':
                    self.explore(i+direction[0], j+direction[1], grid)
                    
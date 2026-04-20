class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # add all initially rotten fruits to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        max_value = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                else:
                    max_value = max(grid[r][c], max_value)

        return max(0, max_value - 2)

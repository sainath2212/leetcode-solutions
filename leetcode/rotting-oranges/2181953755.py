class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rotten = []
        fresh = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    rotten.append((i, j, 0))
                elif grid[i][j]==1:
                    fresh+=1 
        mins = 0 
        while rotten:
            x, y, mins = rotten.pop(0)
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y 
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    fresh-=1 
                    grid[nx][ny] = 2 
                    rotten.append((nx, ny, mins+1))
        return -1 if fresh>0 else mins
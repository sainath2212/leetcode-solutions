class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0]==")":
            return False 
        if grid[rows-1][cols-1]=="(": 
            return False 
        if (rows+cols-1)%2==1: 
            return False 
        dp = {}
        def recur(r, c, bal):
            if r>=rows or c>=cols:
                return False 
            if grid[r][c]=="(":
                bal+=1 
            else:
                bal-=1 
            if bal<0: 
                return False
            if r==rows-1 and c==cols-1:
                return bal==0 
            if (r, c, bal) in dp: 
                return dp[(r, c, bal)]
            down = recur(r+1,c,bal)
            right = recur(r, c+1, bal)
            dp[(r, c, bal)] = down or right 
            return dp[(r, c, bal)]
        return recur(0, 0, 0)
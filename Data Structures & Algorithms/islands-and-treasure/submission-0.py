class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c,dist):
            if (r<0 or c< 0 or r>= rows or c >= cols or grid[r][c] == -1):
                return
            if dist > grid[r][c]:
                return
            grid[r][c] = dist
            dfs(r+1,c,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r,c-1,dist+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r,c,0)
        
        
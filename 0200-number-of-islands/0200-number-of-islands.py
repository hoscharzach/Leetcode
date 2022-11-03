class Solution:      
            
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        dir = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        # iterate through all islands, increase count by 1 when we encounter a 1 and change it to 2
        
        def markLand(grid, row, col):
            if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1":
                grid[row][col] = "2"
                for x, y in dir:
                    markLand(grid, row + x, col + y)
            else:
                return
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    markLand( grid, row, col)
                    
        return islands
                    
        
                    
                


                
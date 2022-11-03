func numIslands(grid [][]byte) int {
    islands := 0
    for i := range grid {
        for j := range grid[i] {
            curr := string(grid[i][j])
            if curr == "1" {
                islands += 1
                markLand(grid, i, j)
            }
            
        }
    }
    return islands
}

func markLand(grid [][]byte, i int, j int) {
    
    a := [][]int{
        {0, 1}, {1, 0}, {-1, 0}, {0, -1},
    }
    
    if i >= 0 && i < len(grid) && j >= 0 && j < len(grid[0]) && string(grid[i][j]) == "1" {
        // fmt.Println(grid[i][j])
        grid[i][j] = 50
        for _, y := range(a) {
        markLand(grid, i + y[0], j + y[1])
        }
    } else {
        return
    } 
    
    
    
     
}
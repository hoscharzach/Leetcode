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
    
    // make new slice of directions
    a := [][]int{
        {0, 1}, {1, 0}, {-1, 0}, {0, -1},
    }
    
    // conditionals for checking if the node is a valid node
    if i >= 0 && i < len(grid) && j >= 0 && j < len(grid[0]) && string(grid[i][j]) == "1" {
        
        // set the node to byte "2"
        grid[i][j] = 50
        // iterate through directions and recursively call markLand on each direction
        for _, y := range(a) {
        markLand(grid, i + y[0], j + y[1])
        }
    } else {
        // if it's not a valid node, then just return
        return
    } 
    
    
    
     
}
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func maxDepth(root *Node) int {
    if root == nil {
        return 0
    }
    var max int = 0
    
    for _, b:= range root.Children {
        c := maxDepth(b)
        if c > max {
            max = c
        } 
        // max = math.Max(max, maxDepth(b))
    }
    
    return 1 + max
}
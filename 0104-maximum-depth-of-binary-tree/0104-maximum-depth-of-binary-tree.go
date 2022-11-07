/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil{
        return 0
    }
    
    // return int(math.Max(float64(1 + maxDepth(root.Left)), float64(1 + maxDepth(root.Right))))
    
    x := 1 + maxDepth(root.Left)
    y := 1 + maxDepth(root.Right)
    
    if x > y {
        return x
    } else {
        return y
    }
}
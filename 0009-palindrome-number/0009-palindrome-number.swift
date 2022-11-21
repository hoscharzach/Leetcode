class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        let str = String(x)
        
        print(str)
        
        return str == String(str.reversed())
    }
}
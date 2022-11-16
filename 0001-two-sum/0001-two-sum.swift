class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var seenNumbers: [Int:Int] = [:]
        // var complement: Int
        
        for (i, v) in nums.enumerated() {
            if (seenNumbers[target - v] != nil && i != seenNumbers[target - v]) {
                
                if let unwrapped = seenNumbers[ target - v] {
                    return [i, unwrapped]
                }
                // print(test)
                // return [i, complement]
            } else {
                seenNumbers[v] = i
            }
            
        }
        print(seenNumbers)
        return [1, 1]
    }
}
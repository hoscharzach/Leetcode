class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var seen:[Int: Int] = [:]
        for (i, num) in nums.enumerated() {
            if (seen[target - num] != nil && seen[target - num] != i) {
                return [i, seen[target - num]!]
            } else {
                seen[num] = i
            }
        }
        
        return []
    }
}





// var seenNumbers: [Int:Int] = [:]
        
//         for (i, v) in nums.enumerated() {
//             if (seenNumbers[target - v] != nil && i != seenNumbers[target - v]) {
                
//                 return [i, seenNumbers[target - v]!]
//                 // if let unwrapped = seenNumbers[ target - v] {
//                 //     return [i, unwrapped]
//                 // }
//             } else {
//                 seenNumbers[v] = i
//             }
            
//         }
//         print(seenNumbers)
//         return [1, 1]
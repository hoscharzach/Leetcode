class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        if strs.isEmpty { return [] }

        var grouped: [String:[String]] = [:]
        
        for str in strs {
            var sorted = String(str.sorted())
            if grouped[sorted] == nil {
                grouped[sorted] = [str]
            } else {
                var existingSort = grouped[sorted]!
                existingSort.append(str)
                grouped[sorted] = existingSort
                // grouped[existingSort].append(str)
            }
            
        }
        
        return Array(grouped.values)
        // var a = [[String]]()
        //     for x in grouped.values {
        //         a.append(x)
        //     }
        //     return a
//         for (i, letter) in alphabet.enumerated() {
//             mappings[letter] = i
//         }
        
//         for word in strs {
//             var pattern: [Int] = []
//             for letter in word {
//                 if let unwrapped = mappings[letter] {
//                     print(unwrapped)
//                 } else {
//                     if let unwrapped = mappings[letter] {
//                         print(unwrapped)
//                     }
//                     // pattern[mappings[letter] = letter]
//                 }
//             }
            
            // var joined = pattern.joined(seperator: "")
            // if grouped[joined] != nil {
            //     grouped[joined].append(word)
            // } else {
            //     grouped[joined] = [word]
            // }
        // }
        
        // print(grouped)
//         var group: [String:[String]] = [:]
//         for word in strs {
//             var pattern = [Int]
//             for letters in word {
//                 if 
//             }
            
//         }
//         print(group)
        
        return [["hello"]]
    }   
}
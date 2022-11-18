class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        
        // gaurd clause
        if strs.isEmpty { return [] }
    
        // declare dictionary to keep track of types of words
        var grouped: [String:[String]] = [:]
        
        
        // iterate through words in strs
        for str in strs {
            
            // sort the word to find the pattern and match it
            var sorted = String(str.sorted())
            
            // if our dictionary does not have an entry at the sorted word, create it and append current word
            if grouped[sorted] == nil {
                grouped[sorted] = [str]
            } else {
                // otherwise access the array already there (it's an optional so we need ! to unwrap it)
                var existingSort = grouped[sorted]!
                
                // append the current word we're on
                existingSort.append(str)
                
                // then set the value of this key to the array with newly appended value on it
                grouped[sorted] = existingSort
                
            }
            
        }
        
        // return a new Array from the values of our dictionary
        return Array(grouped.values)
        
        // can also work
        var a: [[String]] = []
        for value in grouped.values {
            a.append(value)
        }
        
        return a
    
    }   
}
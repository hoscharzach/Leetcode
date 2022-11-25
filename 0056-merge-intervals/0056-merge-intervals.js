/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    // sort intervals by starting point
    let sorted = intervals.sort((a,b) => a[0] - b[0])
    
    // keep track of curr element
    // if current overlaps with next element
    // make new element where start is smallest and end is biggest
    
    // curr start is equal to next start they overlap, new element start = value, new element end = greater value
    // curr end is greater than start next 
    let ans = []
    let i = 0
    while (sorted[i]) {
        let curr = sorted[i]
        let next = sorted[i + 1]
        
        
        if (curr[1] >= next?.[0]) {
            let min = curr[0]
            let max = Math.max(curr[1], next[1])
            sorted.splice(i, 2, [min, max])
                    
        } else {
            i++
        }
    
        
    }
    return sorted
};
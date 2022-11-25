class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def myKey(el):
            return el[0]
        intervals.sort(key=myKey)
        
        ans = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_start, last_end = ans[-1]
            
            if last_end >= start:
                ans[-1] = [
                    last_start,
                    max(last_end, end)
                ]
            else:
                ans.append([start, end])
        
        return ans
        
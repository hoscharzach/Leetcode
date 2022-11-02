class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        
        l, r = 0, 1
        longest = 1
        curr = 1
        while l < len(s):
            new_set = {s[l]}
            while r < len(s) and s[r] not in new_set:
                new_set.add(s[r])
                curr += 1
                r += 1            
                longest = max(curr, longest)
            
            l += 1
            r = l + 1
            curr = 1
        
        return longest
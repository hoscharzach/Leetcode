class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curr_min, curr_max = 1, 1
        
        for num in nums:

            tmp = curr_max * num
            curr_max = max(num * curr_max, num, num * curr_min)
            curr_min = min(num, curr_min * num, tmp)
            res = max(res, curr_max)
        
        return res
                
    
    
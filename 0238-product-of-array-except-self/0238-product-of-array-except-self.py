class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        leftProduct = 1
        for i in range(len(nums)):
            res[i] *= leftProduct
            leftProduct *= nums[i]
        
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        
        return res
            
            
            
        
        
        

        

# [1, 2, 3, 4]
# [1, 2, 6, 24]
# [24, 24, 12, 4]
# [24, 12, 8, 6]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_val = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_val = max(max_val, curr_sum)
            
        return max_val
        
#         maxVal = nums[0]
        
#         for i in range(len(nums)):
#             # print(nums[i], "CURRENT NUM")
#             currSum = nums[i]
#             maxVal = max(currSum, maxVal)
#             for j in range(i + 1, len(nums)):
#                 currSum += nums[j]
#                 maxVal = max(currSum, maxVal)
                
#         return maxVal

        
                
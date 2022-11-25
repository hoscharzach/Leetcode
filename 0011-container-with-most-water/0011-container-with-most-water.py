class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # keep track of max area
         
        
        l, r = 0, len(height) - 1
        
        maxWater = (r - l) * min(height[l], height[r])
        
        while l < r:
            maxWater = max(min(height[l], height[r]) * (r - l), maxWater)        
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
            
        return maxWater
            
            
            
#         for i in range(len(height)):
            
#             for j in range(i + 1, len(height)):
#                 curr = 0
#                 h = min(height[i], height[j])
#                 w = j - i
#                 curr = h * w
#                 maxWater = max(maxWater, curr)
                
        
#         return maxWater
            # h = min(height[l], height[r])
            # w = r - l
            # curr = h * w
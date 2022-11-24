class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #initialize answer array
        ans = []
        
        #sort nums to easily increment or decrement l/r
        nums.sort()
        
        #iterate through list
        for i, v in enumerate(nums):
            
            # if not first element and it's same as one before it, then skip
            if i > 0 and v == nums[i - 1]:
                continue
            
            # do three sum by doing two sum + curr element
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sum = v + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
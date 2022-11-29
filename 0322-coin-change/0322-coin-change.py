class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
    
#         min_coins = [amount + 1] * (amount + 1)
#         min_coins[0] = 0
        
#         for amt in range(1, amount + 1):
#             for c in coins:
#                 if amt - c >= 0:
#                     print(amt, c)
#                     min_coins[amt] = min(min_coins[amt], (1 + min_coins[amt - c]))
        
#         print(min_coins)
#         print(min_coins[amount])
#         return min_coins[amount] if min_coins[amount] != amount + 1 else -1
#         # return min_coins[amt] if min_coins[amt] != 0 else -1
            
            
            
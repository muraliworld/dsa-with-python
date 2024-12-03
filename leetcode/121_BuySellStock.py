from typing import List


class Solution:
    def maxProfit(prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell-buy)
            else:
                buy = sell
        return profit

list = [3,8,1,4,7,5]

print(Solution.maxProfit(list))

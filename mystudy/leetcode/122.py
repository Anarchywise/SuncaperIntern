from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for index, element in enumerate(prices):
            if index == len(prices) - 1:
                return total
            change = prices[index + 1] - prices[index]
            if change > 0:
                total += change
        return total

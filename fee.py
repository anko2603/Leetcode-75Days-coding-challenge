# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold = -prices[0]  
        cash = 0           
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash


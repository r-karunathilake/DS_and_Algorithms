""" Question 121: Best Time to Buy and Sell Stock 

Description: You are given an array prices where prices[i] is the price of a 
             given stock on the ith day. You want to maximize your profit by 
             choosing a single day to buy one stock and choosing a different 
             day in the future to sell that stock. Return the maximum profit 
             you can achieve from this transaction. If you cannot achieve any 
             profit, return 0.

Constraints:
               1 <= prices.length <= 10^5
               0 <= prices[i]     <= 10^4
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    # Assume first price is the minimum 
    min_price = prices[0]
    max_profit = 0
    for current_price in prices[1:]:
        # Calculate the minimum price 
        min_price = min(min_price, current_price)

        # Calcualate the maximum profit
        max_profit = max(max_profit, current_price - min_price)
    return max_profit

def maxProfitBrute(prices: List[int]) -> int:
    max_profit = 0
    for i, current_price in enumerate(prices):
        for future_price in prices[i+1:]:
            current_profit = future_price - current_price
            if current_profit < max_profit:
                continue
            max_profit = current_profit
    
    return max_profit

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestListMerge(unittest.TestCase):
    def test_profit_stock(self):
        # Buy stock on day 2 (index: 1 @ price: $1)
        # Sell stock on dat 5 (index: 4 @ price: $6)
        # Profit is $5 ($6 - $1)
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5)
    
    def test_no_profit_stock(self):
        # Price keeps goin down, no profit can be realized 
        self.assertEqual(maxProfit([7, 6, 4, 3, 1]), 0)

if __name__ == "__main__":
    unittest.main() 

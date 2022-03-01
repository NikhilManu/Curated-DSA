# O(N) Time | O(1) Space 

def maxProfit(prices):
    profit, buy = 0, float('inf')
    for price in prices:
        buy = min(buy, price)
        profit = max(profit, price - buy)
        
    return profit
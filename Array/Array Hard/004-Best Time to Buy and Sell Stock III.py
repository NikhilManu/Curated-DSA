# Time O(N) | Space O(1)

def maxProfit(prices):
    firstProfit, firstBuy = 0, float('inf')
    secondProfit, secondBuy = 0, float('inf')
    for price in prices:
        firstBuy = min(firstBuy, price)
        firstProfit = max(firstProfit, price - firstBuy)
        secondBuy = min(secondBuy, price - firstProfit)
        secondProfit = max(secondProfit, price - secondBuy)
        
    return secondProfit

"""
Intution:
    Suppose you make some profit p1 by doing your first transaction in the stock market. 
    Now you are excited to purchase another stock to earn more profit. Suppose the price of the second stock you aim to buy is x. 
    Now, for you, the net effective price that you are spending from your pocket for this stock will be x-p1, because you already have p1 bucks in your hand. 
    Now, if you sell the second stock at price y your net profit p2 will be p2 = y - (x-p1). You have to do nothing but maximize this profit p2


Doubt which can come to mind:

    => when we get firstProfit, are we going to buy second time from the same price? 
          0  1  2  3
        [10, 3, 6, 10]
        After getting profit at index 2, will we buy index 2 itself?

        No, it seems like we are buying the index 2 again but if you calculate the values we can see that is not the case.
        we will get a profit of 3 at index 2 ( Buy at index 1 and sell at index 2)
        so now,
             firstBuy = 3, firstProfit = 3
             SecondBuy = (6 - 3), SecondProfit = 3

        So if you encounter a new minimum FirstProfit, for the same index the SecondProfit will be same as the new minimum firstProfit
"""
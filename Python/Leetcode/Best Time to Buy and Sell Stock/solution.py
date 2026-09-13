class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit=0
        min_price=float('inf')
        for i in prices:
            if i< min_price:
                min_price=i
            elif (i-min_price) >max_profit:
                max_profit = i-min_price
        return max_profit
        
# Ready to run code ==> 
#  :)      
# def maxProfit(prices) :
#         if not prices:
#             return 0
#         max_profit=0
#         min_price=float('inf')
#         for i in prices:
#             if i< min_price:
#                 min_price=i
#             elif (i-min_price) >max_profit:
#                 max_profit = i-min_price
#         return max_profit
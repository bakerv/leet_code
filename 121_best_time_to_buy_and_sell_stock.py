class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # initialize tracking with 0 profit potential
        global_min = 10000
        max_profit = 0

        for value in prices:
            # check profitablity off selling at the current price
            current_profit = value - global_min
            max_profit = max(max_profit, current_profit)

            # check if there is a lower purchase price
            global_min = min(global_min, value)
        return max_profit
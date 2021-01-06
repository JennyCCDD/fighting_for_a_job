class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for index, i in enumerate(prices[:-1]):
            if prices[index] < prices[index+1]:
                profit_i = prices[index+1] - prices[index]
                profit +=profit_i
        return profit

solution = Solution()
result = solution.maxProfit([7,1,5,3,6,4])
print(result)
# Created by Andres Vargas at 2026/01/18 21:55
# leetgo: 1.4.16
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
         i
        [3,2,6,5,0,3]
         b=2  s=-inf

           b s
        """

        b = float("inf")
        s = 0
        for i in prices:
            if i < b:
                b = i
            profit = i - b

            if profit > s:
                s = profit
        return s


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))

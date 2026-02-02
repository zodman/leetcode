# Created by Andres Vargas at 2026/02/01 21:50
# leetgo: 1.4.16
# https://leetcode.com/problems/majority-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d.setdefault(i,0)
            d[i]+=1

            if d[i] > len(nums)//2:
                return i

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().majorityElement(nums)
    print("\noutput:", serialize(ans, "integer"))

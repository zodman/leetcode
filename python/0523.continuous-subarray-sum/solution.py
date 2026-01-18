# Created by Andres Vargas at 2026/01/12 22:29
# leetgo: 1.4.16
# https://leetcode.com/problems/continuous-subarray-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pass
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().checkSubarraySum(nums, k)
    print("\noutput:", serialize(ans, "boolean"))

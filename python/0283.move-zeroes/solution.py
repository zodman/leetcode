# Created by Andres Vargas at 2026/01/13 22:03
# leetgo: 1.4.16
# https://leetcode.com/problems/move-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                last = i
            else:
                nums[i], nums[last] = nums[last], nums[i]
                last = i


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().moveZeroes(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))

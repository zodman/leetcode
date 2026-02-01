# Created by Andres Vargas at 2026/01/13 22:03
# leetgo: 1.4.16
# https://leetcode.com/problems/move-zeroes/

from typing import *
from leetgo_py import *
import debug_dsa as dsa


# @lc code=begin


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while l < len(nums) - 1:
            if nums[l] == 0:
                r = l+1
                while r < len(nums)-1 and  nums[r] == 0:
                    r+=1
                nums[r], nums[l] = nums[l], nums[r]
            dsa.tpprint(nums, l, r)
            l+=1
        return nums


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().moveZeroes(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))

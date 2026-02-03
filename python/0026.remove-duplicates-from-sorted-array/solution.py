# Created by Andres Vargas at 2026/01/15 21:01
# leetgo: 1.4.16
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import *
from leetgo_py import *
import debug_dsa as d

# @lc code=begin


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        d.tp(nums, l, r)
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeDuplicates(nums)
    s = serialize(ans, "List[int]")
    assert str(ans) == s
    print("\noutput:", ans)

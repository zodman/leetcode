# Created by Andres Vargas at 2026/01/15 21:01
# leetgo: 1.4.16
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import *
from leetgo_py import *
import debug_dsa

# @lc code=begin


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while l < len(nums) - 1:
            while r < len(nums) - 1 and nums[l] == nums[r]:
                r += 1
            nums[l + 1], nums[r] = nums[r], nums[r]
            l += 1
            debug_dsa.tp(nums, l, r)
        return nums


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeDuplicates(nums)
    print("\noutput:", serialize(ans, "integer"))

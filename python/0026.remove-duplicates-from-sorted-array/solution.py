# Created by Andres Vargas at 2026/01/15 21:01
# leetgo: 1.4.16
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        0 1 2 1 2 2
            l   r
        """
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeDuplicates(nums)
    print("\noutput:", serialize(ans, "integer"))

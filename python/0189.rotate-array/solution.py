# Created by Andres Vargas at 2026/01/21 19:59
# leetgo: 1.4.16
# https://leetcode.com/problems/rotate-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        #Input: nums = [1,2,3,4,5,6,7], k = 3
                        ^     ^     ^ i=0
                          ^     ^     i=1
                            ^     ^   i=2
                              ^     ^ i=3  7//3 = 2
        ANSWER         [5,6,7,1,2,3,4]
        """
        nums[:] = nums[len(nums) - k :] + nums[:k]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    Solution().rotate(nums, k)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))

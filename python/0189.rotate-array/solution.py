# Created by Andres Vargas at 2026/01/21 19:59
# leetgo: 1.4.16
# https://leetcode.com/problems/rotate-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    rotate(nums, k)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))

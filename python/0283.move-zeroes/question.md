# [283. Move Zeroes][link] (Easy)

[link]: https://leetcode.com/problems/move-zeroes/

Given an integer array, move all `0`'s to the end of it while maintaining the relative order
of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example 1:**

```
Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]
```

**Example 2:**

```
Input: nums = [0]
Output: [0]
```

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-2³¹ <= nums[i] <= 2³¹ - 1`

**Follow up:** Could you minimize the total number of operations done?


# Notes 
Taking the advantage of two pointers together

# approx solution 1
0,1,2,3,4
r
l
0,1,0,3,4 find l=0 and r!=0
l
  r
1,0,0,3,4 (0,1) (SWAP) l+=1 r=find next non-zero
  l               
      r
1,3,0,0,4 (1,3)(SWAP) l+=1 r=find next non-zero
    l
        r
1,3,0,0,4 (2,4)(SWAP)
1,3,4,0,0 (SWAP) l+=1 r=find next non-zero

# sol 2
r
l
1,0,0
r l
# sol 3
r
l
1,0,1
r l
  r l



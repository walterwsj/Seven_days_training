import sys
from typing import List

"""

"""


def max_area(self, height: List[int]) -> int:
    res, len_nums = 0, len(height)
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            res = max(res, min(height[j], height[i]) * (j - i))
    return res


def max_area_opti(self, height: List[int]) -> int:
    i, j, res = 0, len(height) - 1, 0
    while i < j:
        if height[i] < height[j]:
            min_height = height[i]
            i += 1
        else:
            min_height = height[j]
            j -= 1
        res = max(res, min_height * (j - i + 1))
    return res


def largest_rectangle_area(self, heights: List[int]) -> int:
    res, len_nums = 0, len(heights)
    for i in range(len_nums):
        for j in range(i, len_nums):
            min_height = sys.maxsize
            for k in range(i, j + 1):
                min_height = min(min_height, heights[k])
            res = max(res, min_height * (j - i + 1))
    return res


def largest_rectangle_area_op_1(self, heights: List[int]) -> int:
    res, len_nums = 0, len(heights)
    for i in range(len_nums):
        min_height = sys.maxsize
        for j in range(i, len_nums):
            min_height = min(min_height, heights[j])
            res = max(res, min_height * (j - i + 1))
    return res


def largest_rectangle_area_op_2(heights: List[int]) -> int:
    heights = [0] + heights + [0]
    res, len_nums, stack = 0, len(heights), [-1]
    for i in range(len_nums):
        while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
            res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    return res


def largest_rectangle_area_op_3(heights: List[int]) -> int:
    res, len_nums, stack = 0, len(heights), [-1]
    for i in range(len_nums):
        while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
            res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    while stack[-1] != -1:
        res = max(res, heights[stack.pop()] * (len(heights) - 1 - stack[-1]))
    return res


def three_sum(self, nums: List[int]) -> List[List[int]]:
    res, n = [], len(nums)
    nums.sort()
    for i in range(n):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
    return res


def climb_stairs(self, n: int) -> int:
    if n <= 0:
        return 0
    if 1 <= n < 2:
        return 1
    s1, s2 = 1, 1
    for i in range(2, n + 1):
        s1, s2 = s2, s1 + s2
    return s2


a = [1]
print(largest_rectangle_area_op_2(a))

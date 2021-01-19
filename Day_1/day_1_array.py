"""
递归可用的四种情况
1. 二分查找 O(log n) 每个结点访问一次且仅访问一次
2. 二叉树的前中后序遍历 O(n)
3. BFS DFS广度 深度优先遍历 O(n)
4. 归并排序 O(nlog n)
"""
import sys
from typing import List


def get_fib_n(n):
    if n < 2:
        return 1
    return get_fib_n(n - 1) + get_fib_n(n - 2)


def get_fib_no_recurse(n):
    if n < 1:
        return 0
    if 1 <= n <= 2:
        return 2
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return a


def binary_search(num_list, target):
    start, end = 0, len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == num_list[mid]:
            return True
        elif target > num_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


def binary_search_recurse(num_list, target):
    if len(num_list) == 0:
        return False
    else:
        mid = len(num_list) // 2
        if num_list[mid] == target:
            return True
        elif num_list[mid] < target:
            return binary_search_recurse(num_list[mid + 1:], target)
        else:
            return binary_search_recurse(num_list[:mid], target)


def two_nums_sum(num_list, target):
    len_nums, res = len(num_list), []
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            if num_list[i] + num_list[j] == target:
                res.append([i, j])
    return res


def three_nums_sum_regular(num_list):
    res, len_list, = [], len(num_list)
    for i in range(len_list - 2):
        for j in range(i + 1, len_list - 1):
            for k in range(j, len_list):
                if num_list[i] + num_list[j] + num_list[k] == 0:
                    res.append((num_list[i], num_list[j], num_list[k]))
    return res


def three_nums_sum_optimize(num_list):
    if len(num_list) < 3:
        return None
    num_list.sort()
    res, len_num = [], len(num_list)
    for i in range(len_num):
        if num_list[i] > 0:
            break
        if i > 0 and num_list[i] == num_list[i - 1]:
            continue
        j = i + 1
        k = len_num - 1
        while j < k:
            if num_list[i] + num_list[j] + num_list[k] == 0:
                res.append((num_list[i], num_list[j], num_list[k]))
                while j < k and num_list[j] == num_list[j + 1]:
                    j += 1
                while j < k and num_list[k] == num_list[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif num_list[i] + num_list[j] + num_list[k] < 0:
                j += 1
            else:
                k -= 1
    return res


def move_zero(num_list):
    i = 0
    for j in range(len(num_list)):
        if num_list[j] != 0:
            if i != j:
                num_list[i], num_list[j] = num_list[j], num_list[i]
            i += 1
    return num_list


def get_max_container_regular(num_list):
    len_num, res = len(num_list), 0
    for i in range(len_num - 1):
        for j in range(i + 1, len_num):
            res = max(res, min(num_list[i], num_list[j]) * (j - i))
    return res


def get_max_container_optimize(num_list):
    len_num, res = len(num_list), 0
    left, right = 0, len_num - 1
    while left < right:
        if num_list[left] < num_list[right]:
            tmp_height = num_list[left]
            left += 1
        else:
            tmp_height = num_list[right]
            right -= 1
        res = max(res, tmp_height * (right - left))
    return res


def get_max_area_regular(num_list):
    res, len_num = 0, len(num_list)
    for i in range(len_num - 1):
        for j in range(i, len_num):
            min_height = sys.maxsize
            for k in range(i, j + 1):
                min_height = min(num_list[k], min_height)
            res = max(res, min_height * (j - i + 1))
    return res


def get_max_area_regular_opti(num_list):
    res, len_num = 0, len(num_list)
    for i in range(len_num - 1):
        min_height = sys.maxsize
        for j in range(i, len_num):
            min_height = min(min_height, num_list[j])
            res = max(res, min_height * (j - i + 1))
    return res


def get_max_area_optimize(num_list):
    len_num, stack, res = len(num_list), [-1], 0
    for i in range(len_num):
        while stack[-1] != -1 and num_list[i] <= num_list[stack[-1]]:
            res = max(res, num_list[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    while stack[-1] != -1:
        res = max(res, num_list[stack.pop()] * (stack[-1] - 1))
    return res


a = [-1, 0, 1, 2, -1, -4]
print(three_nums_sum_optimize(a))

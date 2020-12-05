"""
递归可用的四种情况
1. 二分查找 O(log n) 每个结点访问一次且仅访问一次
2. 二叉树的前中后序遍历 O(n)
3. BFS DFS广度 深度优先遍历 O(n)
4. 归并排序 O(nlog n)
"""


def get_fib_n(n):
    if n < 2:
        return 1
    return get_fib_n(n - 1) + get_fib_n(n - 2)


def get_fib_n_1(n):
    if n <= 0:
        return 0
    if 0 < n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        res = a + b
        a = b
        b = res
    return a


def get_fib_n_2(n):
    if n < 1:
        return 0
    if 1 <= n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        res = a + b
        a = b
        b = res
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


print(binary_search_recurse([1, 2, 3, 4, 5, 6], 1))

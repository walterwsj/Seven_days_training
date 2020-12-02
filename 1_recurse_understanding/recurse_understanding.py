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
    for i in range(3, n+1):
        res = a + b
        a = b
        b = res
    return a


print(get_fib_n_1(6))

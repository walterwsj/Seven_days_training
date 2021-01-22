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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Link:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.last = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == self.size:
            self.last.next = node
            self.last = node
        else:
            pre_node = self.get_node(index - 1)
            node.next = pre_node.next
            pre_node.next = node
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")
        if index == 0:
            node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            node = self.last
            pre_node = self.get_node(index - 1)
            pre_node.next = None
            self.last = pre_node
        else:
            pre_node = self.get_node(index - 1)
            next_node = pre_node.next.next
            node = pre_node.next
            pre_node.next = next_node
        self.size -= 1
        return node

    def get_node(self, param):
        tmp = self.head
        while param:
            tmp = tmp.next
            param -= 1
        return tmp

    def reverse_link(self):
        pre = self.head
        cur = self.head.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.head.next = None
        self.head = pre

    def is_circle(self):
        p1, p2 = self.head, self.head
        while p1 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    def circle_length(self):
        p1, p2 = self.head, self.head
        while p1 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        res, backup_node = 0, p1
        while p1.next != backup_node:
            res += 1
            p1 = p1.next
        return res

    def cross_point(self):
        p1, p2 = self.head, self.head
        while p1 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        p2 = self.head
        while p1 != p2:
            p1.next = p1
            p2.next = p2
        return p1

    def swap_pair_recurse(self, head):
        if head is None or head.next is None:
            return head
        next_node = head.next
        head.next = self.swap_pair_recurse(next_node.next)
        next_node.next = head
        return next_node

    def swap_pair(self):
        node = Node(-1)
        a, b, node.next, tmp = node, node, node, self.head
        while b.next != None and b.next.next != None:
            a, b = a.next, b.next.next
            tmp.next, a.next, b.next = b, b.next, a
            tmp, b = a, a
        return node.next

    def reverse_k_group_stack(self, k):
        dummy = Node(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = self.head
            while tmp and count:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            if count:
                p.next = self.head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = tmp
            self.head = tmp
        return dummy.next

    def reverse_k_group_tail(self, k):
        dummy = Node(0)
        dummy.next = self.head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
            pre = self.head
            tail = self.head
        return dummy.next


def reverse_k_group_recurse(head, k):
    cur = head
    count = 0
    while cur and count != k:
        cur = cur.next
        count += 1
    if count == k:
        cur = reverse_k_group_recurse(cur, k)
        while count:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            count -= 1
        head = cur
    return head


a = [1]
print(largest_rectangle_area_op_2(a))

import sys

# Link related
"""
反转一个单链表
"""


class Node:
    def __init__(self, data=0, next_=None):
        self.data = data
        self.next = next_


def reverse(head):
    if head is None:
        return head
    pre, cur = head, head.next
    while cur.next:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    head.next = None
    return pre


"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
"""


def swa_pairs_recurse(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    head.next = swa_pairs_recurse(next_node.nex)
    next_node.next = head
    return head


def swa_pairs(head):
    if head is None or head.next is None:
        return head
    dummy = Node(-1)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        start = pre.next
        end = pre.next.next
        pre.next = end
        start.next = end.next
        end.next = start
        pre = start
    return dummy.next


"""
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
"""


def reverse_k_group_stack(head, k):
    if head is None or head.next is None:
        return head
    dummy = Node(0)
    p = dummy
    while True:
        stack, count, tmp = [], k, head
        while count and tmp:
            stack.append(tmp)
            tmp = tmp.next
            count -= 1
        if count:
            p.next = head
            break
        while stack:
            p.next = stack.pop()
            p = p.next
        p.next = tmp
        head = tmp
    return dummy.next


def reverse_k_group_tail(head, k):
    if head is None or head.next is None:
        return head
    dummy = Node(0)
    dummy.next = head
    pre, end = dummy, dummy
    while True:
        count = k
        while count and end:
            end = end.next
            count -= 1
        if not end:
            break
        head = pre.next
        while pre.next != end:
            cur = pre.next
            pre.next = cur.next
            cur.next = end.next
            end.next = cur
        pre = head
        end = head
    return dummy.next


def reverse_k_group_recurse(head, k):
    if head is None or head.next is None:
        return head
    count = 0
    cur = head
    while count != k and cur:
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


if __name__ == '__main__':
    l1 = Node(1)  # 建立链表3->2->1->9->None
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)

    print(reverse_k_group_tail(l1, 3))

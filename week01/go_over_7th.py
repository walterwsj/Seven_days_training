class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def swap_pairs(head):
    if head is None and head.next is None:
        return head
    dummy = Node(0)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        start = pre.next
        end = pre.next.next
        pre.next = start.next
        start.next = end.next
        end.next = start
        pre = start
    return dummy.next


def swap_pairs_recurse(head):
    if head is None and head.next is None:
        return head
    next_node = head.next
    head.next = swap_pairs_recurse(next_node.next)
    next_node.next = head
    return head


def swap_k_group(head, k):
    if head is None and head.next is None:
        return head
    dummy = Node(0)
    dummy.next = head
    pre, tail = dummy, dummy
    while True:
        count = k
        while count and tail:
            tail = tail.next
            count -= 1
        if not tail:
            break
        pre.next = head
        while pre.next != tail:
            cur = pre.next
            pre.next = cur.next
            cur.next = tail.next
            tail.next = cur
        pre = head
        end = head
    return dummy.next

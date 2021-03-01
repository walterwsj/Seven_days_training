class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    pre = Node(0)
    pre.next = head
    tmp = pre
    while tmp.next and tmp.next.next:
        start = tmp.next
        end = tmp.next.next
        tmp.next = end
        start.next = end.next
        end.next = start
        tmp = start
    return pre.next


def reverse(head):
    if head is None:
        return head
    pre = head
    cur = head.next
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    head.next = None
    return pre


def swap_pairs_recurse(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    head.next = swap_pairs_recurse(next_node.next)
    next_node.next = head
    return head


def reverse_k_group(head, k):
    dummy = Node(-1)
    dummy.next = head
    pre, tail = dummy, dummy
    while tail.next:
        count = k
        while tail and count:
            tail = tail.next
            count -= 1
        if not tail:
            break
        next_node = tail.next
        tail.next = None
        start = pre.next
        pre.next = reverse(start)
        start.next = next_node
        pre = start
        tail = start
    return dummy.next


if __name__ == '__main__':
    l1 = Node(1)  # 建立链表3->2->1->9->None
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l1.next.next.next.next = Node(5)

    print(reverse_k_group(l1, 2))

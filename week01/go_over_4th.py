class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Link:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid")
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

    def get_node(self, param):
        tmp_node = self.head
        while param:
            tmp_node = tmp_node.next
            param -= 1
        return tmp_node

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid")
        node = None
        if index == 0:
            node = self.head
            self.head = self.head.next
        elif index == self.size:
            node = self.last
            pre_node = self.get_node(index - 1)
            pre_node.next = None
            self.last = pre_node
        else:
            pre_node = self.get_node(index - 1)
            node = pre_node.next
            pre_node.next = pre_node.next.next
        self.size -= 1
        return node

    def reverse(self):
        pre = self.head
        cur = self.head.next
        while cur.next:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head.next = None
        self.head = pre


def is_circle(link_list):
    p1, p2 = link_list, link_list
    while p1 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False

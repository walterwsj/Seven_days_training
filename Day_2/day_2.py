"""
Array: 在内存中开辟了一段连续的内存空间 通过偏移计算地址实现随机访问 插入删除是很耗时的操作 O(n) 时间复杂度
Link：插入 删除操作很快 O(1) 时间复杂度 除了头尾访问随机结点的时候 O(n)
Skip list: 基于链表且元素有序 对标的是平衡树和二分查找 插入 删除 搜索 都是O(log n)
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("invalid index")
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.last = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif self.size == index:
            self.last.next = node
            self.last = node
        else:
            pre_node = self.get_node(index - 1)
            node.next = pre_node.next
            pre_node.next = node
        self.size += 1

    def get_node(self, param_index):
        if param_index < 0 or param_index > self.size:
            raise ValueError("Invalid param_index")
        tmp = self.head
        while param_index:
            tmp = tmp.next
            param_index -= 1
        return tmp

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")
        node = None
        if index == 0:
            node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            pre_node = self.get_node(index - 1)
            node = pre_node.next
            pre_node.next = None
            self.last = pre_node
        else:
            pre_node = self.get_node(index - 1)
            next_node = pre_node.next.next
            node = pre_node.next
            pre_node.next = next_node
        self.size -= 1
        return node

    def out_put(self):
        res = []
        tmp = self.head
        while tmp:
            res.append(tmp.data)
            tmp = tmp.next
        return res

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

    def is_circled(self):
        p_slow, p_fast = self.head, self.head
        while p_slow and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow == p_fast:
                return True
        return False

    def get_circle_length(self):
        p_slow, p_fast, res = self.head, self.head, 0
        while p_slow and p_slow.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow == p_fast:
                break
        if p_fast is None or p_fast.next is None:
            return 0
        else:
            tmp = p_slow
            while tmp != p_slow.next:
                res += 1
                p_slow = p_slow.next
        return res

    def get_cross_node(self):
        p_slow, p_fast, res = self.head, self.head, 0
        while p_slow and p_slow.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow == p_fast:
                break
        p_slow = self.head
        while p_slow != p_fast:
            p_slow = p_slow.next
            p_fast = p_fast.next
        return p_slow

    def get_last_kth_num(self, k):
        if k < 0:
            raise ValueError("invalid param")
        list_len = self.get_list_length()
        if k > list_len:
            raise ValueError("invalid param")
        elif k == list_len:
            return self.head
        elif k == 0:
            return self.last
        else:
            return self.get_node(list_len - k)

    def get_list_length(self):
        res, cur = 0, self.head.next
        while cur:
            res += 1
            cur = cur.next
        return res

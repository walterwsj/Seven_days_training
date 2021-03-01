"""
1. 树的结点如果出现了环，数据结构便变成了图
2. 链表是特殊化的树， 树是特殊化的图
3. 对二叉搜索树的遍历 中序的结果是升序的 查询 插入和删除都是 O(log n)
为什么遍历树的时候推荐递归
1. 子树和原始树都有着相同的数据结构，因为重复性的原因可以用一个函数来处理
2. 树的定义代表着树无法有效的循环，根节点对子节点的访问是单向的， 符合递归的调用方式
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Tree:
    def __init__(self, node=None):
        self.res = []
        self.root = node

    def pre_order(self, tree):
        if tree:
            self.res.append(tree.val)
            self.pre_order(tree.left)
            self.pre_order(tree.right)
        return self.res

    def pre_order_no_recurse(self, tree):
        stack = []
        while tree or stack:
            while tree:
                self.res.append(tree.val)
                stack.append(tree)
                tree = tree.left
            if stack:
                tmp = stack.pop()
                tree = tmp.right
        return self.res

    def create_tree_by_list(self, num_list):
        self.root = TreeNode(num_list[0])
        len_list = len(num_list)
        index = 1
        queue = [self.root]
        while queue:
            tmp = queue.pop(0)
            if index == len_list:
                break
            if num_list[index]:
                tmp.left = TreeNode(num_list[index])
                queue.append(tmp.left)
            index += 1
            if num_list[index]:
                tmp.right = TreeNode(num_list[index])
                queue.append(tmp.right)
            index += 1
        return self.root

    def create_tree_num_list(self, num_list):
        index, len_list = 1, len(num_list)
        self.root = TreeNode(num_list[0])
        stack = [self.root]
        while stack:
            if index == len_list:
                break
            node = stack.pop(0)
            if num_list[index]:
                node.left = TreeNode(num_list[index])
                stack.append(node.left)
            index += 1
            if index == len_list:
                break
            if num_list[index]:
                node.right = TreeNode(num_list[index])
                stack.append(node.right)
            index += 1
        return self.root

    def breadth_first_search(self, tree):
        queue = [tree]
        while queue:
            tmp = queue.pop(0)
            self.res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return self.res

    def post_order(self, tree):
        if tree:
            self.post_order(tree.left)
            self.post_order(tree.right)
            self.res.append(tree.val)
        return self.res

    def post_order_no_recurse(self, tree):
        stack1, stack2 = [tree], []
        while stack1:
            tmp = stack1.pop()
            stack2.append(tmp.val)
            if tmp.left:
                stack1.append(tmp.left)
            if tmp.right:
                stack1.append(tmp.right)
        while stack2:
            self.res.append(stack2.pop())
        return self.res

    # Tree's level
    def create_tree_by_list_1(self, num_list):
        if len(num_list) == 0:
            return None
        self.root = TreeNode(num_list[0])
        index, len_list = 1, len(num_list)
        queue = [self.root]
        while queue:
            tmp_node = queue.pop(0)
            if index == len_list:
                break
            if num_list[index]:
                tmp_node.left = TreeNode(num_list[index])
                queue.append(tmp_node.left)
            index += 1
            if index == len_list:
                break
            if num_list[index]:
                tmp_node.right = TreeNode(num_list[index])
                queue.append(tmp_node.right)
            index += 1
        return self.root

    def breadth_search_1(self):
        queue = [self.root]
        while queue:
            tmp = queue.pop(0)
            self.res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return self.res

    def post_order_recurse(self, tree):
        if tree:
            self.post_order_recurse(tree.left)
            self.post_order_recurse(tree.right)
            self.res.append(tree.val)

    def post_order_1(self, tree):
        stack_pri, stack_sla = [tree], []
        while stack_pri:
            tmp = stack_pri.pop()
            stack_sla.append(tmp)
            if tmp.left:
                stack_pri.append(tmp.left)
            if tmp.right:
                stack_pri.append(tmp.right)
        while stack_sla:
            self.res.append(stack_sla.pop().val)
        return self.res

    def in_order_1(self, tree):
        stack = []
        while stack or tree:
            while tree:
                stack.append(tree)
                tree = tree.left
            if stack:
                tmp = stack.pop()
                self.res.append(tmp.val)
                tree = tree.right
        return self.res

    def get_deep_binary_tree(self, tree):
        if tree is None:
            return 0
        left_tree = self.get_deep_binary_tree(tree.left)
        right_tree = self.get_deep_binary_tree(tree.right)
        return max(left_tree, right_tree) + 1


if __name__ == "__main__":
    obj = Tree()
    node_list_recurse = [1, 2, 4, None, None, 5, None, None, 6, None, 3]
    my_tree = obj.create_tree_num_list(node_list_recurse)

    res2 = obj.pre_order_no_recurse(my_tree)
    obj.res = []
    res = obj.post_order_no_recurse(my_tree)
    obj.res = []
    res1 = obj.post_order(my_tree)
    print(res2)
    print(res)
    print(res1)

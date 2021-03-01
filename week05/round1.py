import collections

"""
爬楼梯
"""


def get_stairs(n):
    if n < 3:
        return n
    step1, step2 = 1, 2
    for i in range(3, n + 1):
        step1, step2 = step2, step1 + step2
    return step2


"""
位1的个数
"""


def get_bits(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n >>= 1

    return res


def get_bits_py(n):
    return bin(n).count("1")


"""
2次幂
"""


def get_pow(n):
    if n == 0:
        return False
    return n & (n - 1) == 0


"""
颠倒二进制位
"""


def reverse_bits_py(n):
    return int('0b' + bin(n)[2:][::-1] + '0' * (32 - len(bin(n)[2:])), 2)


def reverse_bits(n):
    ans, power = 0, 31
    while n:
        ans += (n & 1) << power
        n >>= 1
        power -= 1
    return ans


"""
字典树
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

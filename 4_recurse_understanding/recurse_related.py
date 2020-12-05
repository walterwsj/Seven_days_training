"""
Recursion Form

def recursion(level,param1,param2):
    # recursion terminator
    if level > MAX_LEVEL:
    process_result
    return

    # process logic in current level
    process(level,data)

    # drill down
    self.recursion(level+1,param1

    # reverse the current level if needed

"""


class MySolution:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array

    def generate_parenthesis(self, left, right, max_level, empty_str):
        if left >= max_level and right >= max_level:
            self.array.append(empty_str)
            return
        if left < max_level:
            self.generate_parenthesis(left + 1, right, max_level, empty_str + '(')
        if right < left:
            self.generate_parenthesis(left, right + 1, max_level, empty_str + ')')


if __name__ == "__main__":
    ms = MySolution()
    ms.generate_parenthesis(0,0, 3, "")
    print(ms.array)

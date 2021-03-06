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


def get_go_upstairs(n):
    if 0 < n <= 2:
        return n
    step_1, step_2, step_res = 1, 2, 0
    for i in range(3, n + 1):
        step_res = step_1 + step_2
        step_1 = step_2
        step_2 = step_res
    return step_res


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


# if __name__ == "__main__":
#     ms = MySolution()
#     ms.generate_parenthesis(0, 0, 3, "")
#     print(ms.array)

print(get_go_upstairs(6))

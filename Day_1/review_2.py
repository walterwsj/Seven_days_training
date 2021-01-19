import sys


def get_fib(n):
    if n == 0:
        return 0
    if 1 <= n <= 2:
        return 1
    first, second = 1, 1
    for i in range(3, n + 1):
        first, second = second, first + second
    return first


def binary_search_recurse(num_list, target):
    if len(num_list) <= 1:
        return False
    mid = len(num_list) // 2
    if num_list[mid] == target:
        return True
    elif num_list[mid] > target:
        return binary_search_recurse(num_list[:mid], target)
    else:
        return binary_search_recurse(num_list[mid + 1:], target)


def binary_search_regular(num_list, target):
    head, rear = 0, len(num_list) - 1
    while head < rear:
        mid = (head + rear) // 2
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            rear = mid - 1
        else:
            head = mid + 1
    return False


def move_zero(num_list):
    j = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            if i != j:
                num_list[i], num_list[j] = num_list[j], num_list[i]
            j += 1
    return num_list


def two_sum(num_list, target):
    res, len_num = [], len(num_list)
    for i in range(len_num - 1):
        for j in range(i + 1, len_num):
            if num_list[i] + num_list[j] == target:
                res.append((num_list[i], num_list[j]))
    return res


def three_nums_sum_regular(num_list):
    res, len_num = set(), len(num_list)
    num_list.sort()
    for i in range(len_num - 2):
        for j in range(i + 1, len_num - 1):
            for k in range(j, len_num):
                if num_list[i] + num_list[j] + num_list[k] == 0:
                    res.add((num_list[i], num_list[j], num_list[k]))
    return res


def three_nums_sum_optimize(num_list):
    num_list.sort()
    res, len_num = [], len(num_list)
    for i in range(len_num):
        if num_list[i] > 0:
            break
        if i > 0 and num_list[i] == num_list[i - 1]:
            continue
        first, last = i + 1, len_num - 1
        while first < last:
            if num_list[i] + num_list[first] + num_list[last] == 0:
                res.append((num_list[i], num_list[first], num_list[last]))
                while first < last and num_list[first] == num_list[first + 1]:
                    first += 1
                while first < last and num_list[last] == num_list[last - 1]:
                    last -= 1
                first += 1
                last -= 1
            elif num_list[i] + num_list[first] + num_list[last] > 0:
                last -= 1
            else:
                first += 1
    return res


def get_max_container_regular(num_list):
    res, len_num = 0, len(num_list)
    for i in range(len_num - 1):
        for j in range(i + 1, len_num):
            res = max(res, min(num_list[i], num_list[j]) * (j - i))
    return res


def get_max_container_optimize(num_list):
    res, len_num = 0, len(num_list)
    left, right = 0, len_num - 1
    while left < right:
        if num_list[left] < num_list[right]:
            height = num_list[left]
            left += 1
        else:
            height = num_list[right]
            right -= 1
        res = max(res, height * (right - left + 1))
    return res


def get_max_area_regular(num_list):
    res, len_num = 0, len(num_list)
    for i in range(len_num - 2):
        for j in range(i + 1, len_num - 1):
            min_height = sys.maxsize
            for k in range(j, len_num):
                min_height = min(num_list[k], min_height)
            res = max(res, min_height * (j - i + 1))
    return res


def get_max_area_optimize_1(num_list):
    res, len_num = 0, len(num_list)
    for i in range(len_num - 1):
        min_height = sys.maxsize
        for j in range(i, len_num):
            min_height = min(min_height, num_list[j])
            res = max(res, min_height * (j - i + 1))
    return res


def get_max_area_optimize_2(num_list):
    res, len_num, stack = 0, len(num_list), [-1]
    for i in range(len_num):
        while stack[-1] != -1 and num_list[i] < num_list[stack[-1]]:
            res = max(res, num_list[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    while stack[-1] != -1:
        res = max(res, num_list[stack.pop()] * (stack[-1] - 1))
    return res


# a = [-1, 0, 1, 2, -1, -4]
result_list = [2, 1, 5, 6, 2, 3]
print(get_max_area_optimize_2(result_list))

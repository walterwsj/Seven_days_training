import sys


def get_fib(n):
    if n == 0:
        return 0
    if 1 <= n <= 2:
        return 1
    former, last = 1, 1
    for i in range(3, n + 1):
        former, last = last, former + last
    return former


def binary_search_recurse(num_list, target):
    if len(num_list) < 2:
        return False
    mid = len(num_list) // 2
    if num_list[mid] == target:
        return True
    elif num_list[mid] > target:
        return binary_search_recurse(num_list[:mid], target)
    else:
        return binary_search_recurse(num_list[mid + 1:], target)


def binary_search_regular(num_list, target):
    start, end = 0, len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


def move_zero(num_list):
    j, len_num = 0, len(num_list)
    for i in range(len_num):
        if num_list[i] != 0:
            if i != j:
                num_list[i], num_list[j] = num_list[j], num_list[i]
            j += 1
    return num_list


def two_sum(num_list, target):
    len_num, res = len(num_list), []
    for i in range(len_num - 1):
        for j in range(i + 1, len_num):
            if num_list[i] + num_list[j] == target:
                res.append((num_list[i], num_list[j]))
    return res


def two_sum_optimize(nums, target):
    dic, res = {}, []
    for index, value in enumerate(nums):
        rest_part = target - value
        if rest_part in dic:
            return [dic[rest_part], index]
        else:
            dic[value] = index


def three_nums_sum_regular(num_list):
    res, len_num = set(), len(num_list)
    num_list.sort()
    for i in range(len_num - 2):
        for j in range(i, len_num - 1):
            for k in range(j + 1, len_num):
                if num_list[i] + num_list[j] + num_list[k] == 0:
                    res.add((num_list[i], num_list[j], num_list[k]))
    return res


def three_nums_sum_optimize(num_list):
    res, len_num = set(), len(num_list)
    num_list.sort()
    for i in range(len_num):
        if num_list[i] > 0:
            break
        if i > 0 and num_list[i] == num_list[i - 1]:
            continue
        j, k = i + 1, len_num - 1
        while j < k:
            if num_list[i] + num_list[j] + num_list[k] == 0:
                res.add((num_list[i], num_list[j], num_list[k]))
                while j < k and num_list[j] == num_list[j + 1]:
                    j += 1
                while j < k and num_list[k] == num_list[k - 1]:
                    k -= 1
                i += 1
                k -= 1
            elif num_list[i] + num_list[j] + num_list[k] > 0:
                k -= 1
            else:
                j += 1
    return res


def get_max_container_regular(num_list):
    len_num, res = len(num_list), 0
    for i in range(len_num - 1):
        for j in range(i + 1, len_num):
            res = max(res, (j - i) * min(num_list[i], num_list[j]))
    return res


def get_max_container_optimize(num_list):
    len_num, res = len(num_list), 0
    i, j = 0, len_num - 1
    while i < j:
        if num_list[i] > num_list[j]:
            height = num_list[j]
            j -= 1
        else:
            height = num_list[i]
            i += 1
        res = max(res, height * (j - i + 1))
    return res


def get_max_area_regular(num_list):
    len_num, res = len(num_list), 0
    for i in range(len_num - 1):
        for j in range(i, len_num):
            min_height = sys.maxsize
            for k in range(i, j + 1):
                min_height = min(min_height, num_list[k])
            res = max(res, min_height * (j - i + 1))
    return res


def get_max_area_opti_1(num_list):
    len_num, res = len(num_list), 0
    for i in range(len_num - 1):
        min_height = sys.maxsize
        for j in range(i, len_num):
            min_height = min(min_height, num_list[j])
            res = max(res, min_height * (j - i + 1))
    return res


def get_max_area_opti_2(num_list):
    stack, len_num, res = [-1], len(num_list), 0
    for i in range(len(num_list)):
        while stack[-1] != -1 and num_list[i] < num_list[stack[-1]]:
            res = max(res, num_list[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    while stack[-1] != -1:
        res = max(res, num_list[stack.pop()] * (stack[-1] - 1))
    return res


# a = [-1, 0, 1, 2, -1, -4]
result_list = [2, 1, 5, 6, 2, 3]
print(get_max_area_opti_2(result_list))

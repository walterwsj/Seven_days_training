"""
Array: 在内存中开辟了一段连续的内存空间 通过偏移计算地址实现随机访问 插入删除是很耗时的操作 O(n) 时间复杂度
Link：插入 删除操作很快 O(1) 时间复杂度 除了头尾访问随机结点的时候 O(n)
Skip list: 基于链表且元素有序 对标的是平衡树和二分查找 插入 删除 搜索 都是O(log n)
"""


def move_zero(num_list):
    un_zero_index = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[un_zero_index] = num_list[i]
            if un_zero_index != i:
                num_list[i] = 0
            un_zero_index += 1
    return num_list


def move_zero_1(num_list):
    tmp_index = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[i], num_list[tmp_index] = num_list[tmp_index], num_list[i]
            tmp_index += 1
    return num_list


def move_zero_2(num_list):
    tmp_index = 0
    len_list = len(num_list)
    for i in range(len_list):
        if num_list[i] != 0:
            num_list[tmp_index] = num_list[i]
            if i != tmp_index:
                num_list[i] = 0
            tmp_index += 1
    return num_list


def move_zero_3(num_list):
    tmp_zero_index = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[tmp_zero_index] = num_list[i]
            if tmp_zero_index != i:
                num_list[i] = 0
            tmp_zero_index += 1
    return num_list


def move_zero_4(num_list):
    tmp_index = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[i], num_list[tmp_index] = num_list[tmp_index], num_list[i]
            tmp_index += 1
    return num_list


def move_zero_5(num_list):
    tmp_index = 0
    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[tmp_index] = num_list[i]
            if i != tmp_index:
                num_list[i] = 0
            tmp_index += 1
    return num_list

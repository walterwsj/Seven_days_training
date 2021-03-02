import datetime
import os
import shutil
import sys
import time
from functools import reduce

"""
Python3中，range返回的是可迭代对象 而不是列表类型 输出不会返回列表
"""
xx = list(range(10))
# print(xx)

"""
在方法内部修改全局变量
"""
a = 1


def update():
    global a
    a = 2


update()
# print(a)

"""
五个基本库 sys;re;os;math;datetime
"""

"""
合并字典 删除键 update del
"""
dic = {"0": "a", "1": "b"}
del dic["0"]
dic1 = {"2": "c"}
dic.update(dic1)
# print(dic)

"""
GIL 全局解释器锁。 统一进程中会有多个线程，如果某一个线程在运行python程序的时候会霸占python解释器，使该进程内的其他线程不能运行python程序。
等该线程运行完之后线程才能运行 但是如果线程在运行的过程中遇到耗时的操作 则解释器锁会解开 允许其他线程运行
多进程中每个进程都会被系统分配资源 相当于每个进程都有一个python解释器 多以多进程可以实现同时运行 缺点系统资源开销大
"""

"""
列表去重的方法 set()
"""

"""
fun(*args,**kwargs) 主要用于函数的定义 将不定量的参数传递给一个参数 不定的意思就是 函数的使用者会传递多少
个参数给你 *args非键值对的可变数量  **kwargs 接收不定长的键值对
"""

"""
什么样的语音可以用装饰器 函数可以作为参数传递的语音 可以使用装饰器
"""

"""
内建的数据类型 整型 布尔 字符串 列表 元组 字典
"""

"""
__new__和__init__区别
init 构造方法 创建对象默认被调用 
new 至少有一个参数cls 代表类；必须有返回值 返回实例化之后的实例 
init 有一个默认参数self 这就是new 返回的实例 init是在new的基础上完成一些初始化的动作 不需要返回值
new 如果创建的是当前类的实例 自动调用init 通过return语句里调用的new函数的第一个参数cls来保证是
当前的实例；这时候如果是其他类的类名 实际返回的就是其他类的实例
"""


# 1. 读取一个jsonline 文件

def get_file():
    with open('file.txt', 'rb') as f:
        return f.readlines()


def get_lines_1():
    res = []
    with open('file.txt', 'rb') as f:
        data = f.readlines(10000)
    res.append(data)
    yield res


# 2, 补充缺失的代码
'''
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
'''


def print_directory_contents(s_path):
    for sub_path in os.listdir(s_path):
        sub_folder_path = os.path.join(s_path, sub_path)
        if os.path.isdir(sub_folder_path):
            print_directory_contents(sub_folder_path)
        else:
            print(sub_folder_path)


# 3. 输入日期， 判断这一天是这一年的第几天？
def get_day_th():
    year = input("Year:")
    month = input("Month: ")
    day = input("Day: ")
    date_input = datetime.date(year=int(year), month=int(month), day=int(day))
    date_base = datetime.date(year=int(year), month=1, day=1)
    return (date_input - date_base).days + 1


# 4.打乱一个排好序的list对象alist？
# alist=[1,2,3,4,5]
# random.shuffle(alist)


# 5现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
# d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
# sorted(d.items(), key=lambda x: x[1])


# 6 字典推导
# d = {key:value for (key,value) in iterable}

# 7 字符串反转 [::-1]

# 8 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
str1 = "k:1|k1:2|k2:3|k3:4"


def str2dict(str1):
    dic = {}
    for items in str1.split('|'):
        k, v = items.split(':')
        dic[k] = v
    return dic


def str2dict_1(str1):
    return {k: v for t in str1.split("|") for k, v in t.split(":")}


# 9.请按alist中元素的age由大到小排序

alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]


def sorted_by_age(list_age):
    return sorted(alist, key=lambda x: x['age'], reverse=True)


# 11.写一个列表生成式，产生一个公差为11的等差数列

# print([x for x in range(0, 100, 11)])

# 12.给定两个列表，怎么找出他们相同的元素和不同的元素？

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# set1 = set(list1)
# set2 = set(list2)
# print(set1 & set2)
# print(set1 ^ set2)

# 13.请写出一段python代码实现删除list里面的重复元素？
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
print(set(l1))

# sorted(key=l1.index)

"""
装饰器
"""


def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@singleton
class Foo(object):
    pass


foo1 = Foo()
foo2 = Foo()

"""
基类
"""


class SingletonBase(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonBase, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(SingletonBase):
    pass


# 18.反转一个整数，例如-123 --> -321
def reverse_num(x):
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] == '-':
        str_x = str_x[1:][::-1]
        x = int(str_x)
        x = -x
    else:
        str_x = str_x[::-1]
        x = int(str_x)
    return x if -2147483648 < x < 2147483647 else 0


# 19.设计实现遍历目录与子目录，抓取.pyc文件

def get_files(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            name, extend_name = os.path.splitext(file)
            if suffix == extend_name:
                res.append(os.path.join(root, file))
    return res


def get_files_dir(test_dir, suffix):
    res = []
    file_list = os.listdir(test_dir)
    for item in file_list:
        if os.path.isfile(item):
            if item.endswith(suffix):
                res.append(item)
        elif os.path.isdir(item):
            get_files_dir(item, suffix)
    return res


# 21.Python-遍历列表时删除元素的正确做法
a = [i for i in range(10)]
b = filter(lambda x: x > 5, a)


# 22.字符串的操作题目
def get_missing_letter(a):
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    s2 = set(a)
    res = "".join(sorted(s1 - s2))
    return res


# 23.可变类型和不可变类型
"""
1. 可变类型有字典，列表；不可变类型有number string 元组tuple
2. 修改操作时，可变类型修改的是内存中的地址 修改的是内存中的值 没有开辟新的内存空间
3. 不可变类型没有修改的是原地址的值，而是开辟了一块新的内存空间，将原地址的内容复制过去
"""

# 24.is和==有什么区别？
"""
is： 比较的是对象的id 比较两个对象是否为同一个实例对象，是否指向同一个地址
==： 比较两个对象的内容还有值是否相等
"""

# 25.求出列表所有奇数并构造新列表
list_int = [i for i in range(10)]
res = [i for i in list_int if i % 2 == 1]

# 26.用一行python代码写出1+2+3+10248
list_a = [1, 2, 3, 10248]
num = sum(list_a)
num1 = reduce(lambda x, y: x + y, list_a)

# 27.Python中变量的作用域？（变量查找顺序)
"""
LEGB
L: local 函数内部
E: enclosing 函数内部还有内嵌函数
G: 全局
B： build-in 内置作用
"""


# 28.字符串 "123" 转换成 123 ，不使用内置api，例如 int()
def get_num(s):
    num = 0
    for i in s:
        for j in range(10):
            if i == str(j):
                num = num * 10 + j
    return num


def get_num_ord(s):
    flag = 0
    for char in s:
        flag = flag * 10 + ord(char) - ord('0')
    return flag


def get_num_reduce(s):
    return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), s)


# 29.Given an array of integers 两数之和


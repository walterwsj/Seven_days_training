import collections
import datetime
import os
import re
import shutil
import sys
import time
from collections import Counter
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


def get_directory(path):
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            res.append(os.path.join(root, file))
    return res


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


def str_dic(test_str):
    result = {}
    for item in test_str.split('|'):
        k, v = item.split(':')
        result[k] = v
    return result


def str_dic_py(test_str):
    return {k: v for t in test_str.split('|') for k, v in t.split(':')}


# 9.请按test_list中元素的age由大到小排序

test_list = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]


def sorted_by_age(list_age):
    return sorted(list_age, key=lambda x: x['age'], reverse=True)


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

"""
单例模式
装饰器
"""


def singleton_decorator(cls):
    instance = {}

    def create(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return create


@singleton_decorator
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

def get_files(path, suffix):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            name, extend_name = os.path.splitext(file)
            if suffix == extend_name:
                result.append(os.path.join(root, file))
    return result


def get_files_dir(test_dir, suffix):
    result = []
    for directory in os.listdir(test_dir):
        if os.path.isfile(directory):
            if directory.endswith(suffix):
                result.append(directory)
        elif os.path.isdir(directory):
            get_files_dir(directory, suffix)
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
    result = 0
    for char in s:
        for number in range(10):
            if char == str(number):
                result = result * 10 + number
    return result


def get_num_ord(s):
    result = 0
    for char in s:
        result = result * 10 + ord(char) - ord('0')
    return result


def get_num_reduce(s):
    return reduce(lambda number, char: number * 10 + ord(char) - ord('0'), s)


# 29.Given an array of integers 两数之和
def get_index(num_list, target):
    result = {}
    for index, value in enumerate(num_list):
        rest = target - value
        if rest in result:
            return [index, result[rest]]
        else:
            result[value] = index
    return result


a_list = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
sorted(a_list, key=lambda x: x['age'], reverse=True)


# 30.python代码实现删除一个list里面的重复元素
def get_list_1(num_list):
    return list(set(num_list))


def get_list_2(num_list):
    result = []
    for char in num_list:
        if char not in result:
            result.append(char)
    return res


def get_list_3(num_list):
    result = {}
    result = result.fromkeys(num_list)
    return list(num_list.keys())


# 31.统计一个文本中单词频次最高的10个单词？
def get_most_common(file_path):
    result = {}
    with open(file_path, 'rb') as f:
        for line in f.readlines():
            line = re.sub(r"\W=", " ", str(line))
            line_one = line.split()
            for key_one in line_one:
                if not result.get(key_one):
                    result[key_one] = 1
                else:
                    result[key_one] += 1
    top_ten = sorted(result, key=lambda x: x[1], reverse=True)
    return [x[0] for x in top_ten]


def get_most_counter(file_path):
    with open(file_path) as f:
        return list(map(lambda word: word[0], Counter(re.sub(r"\w+", " ", f.read()).split()).most_common(10)))


# 32.请写出一个函数满足以下条件
"""
该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
1、该元素是偶数
2、该元素在原list中是在偶数的位置(index是偶数)
"""


def get_list(num_list):
    return [i for i in num_list if i % 2 == 0 and num_list.index(i) % 2 == 0]


# 33.使用单一的列表生成式来产生一个新的列表
list_data = [1, 2, 5, 8, 10, 3, 18, 6, 20]
result = [i for i in list_data if i % 2 == 0]


# 34.用一行代码生成[1,4,9,16,25,36,49,64,81,100
# [i*i for i in range(1,11)]

# 35

# y = int(input("请输入4位数字的年份:"))
# m = int(input("请输入月份:"))
# d = int(input("请输入是哪一天"))
# target_day = datetime.date(y, m, d)
# day_count = target_day - datetime.date(y, 1, 1)
# res = (target_day - day_count).days + 1


# 36.两个有序列表，l1,l2，对这两个列表进行合并不可使用extend

def merge_list(list_1, list_2):
    merge_result = []
    while len(list_1) and len(list_2):
        if list_1[0] < list_2[0]:
            merge_result.append(list_1.pop())
        else:
            merge_result.append(list_2.pop())
    while len(list_1):
        merge_result.append(list_1.pop())
    while len(list_2):
        merge_result.append((list_2.pop()))
    return merge_result


# 37.给定一个任意长度数组，实现一个函数

def func_1(my_list):
    my_list = list(my_list)
    my_list.sort(reverse=True)
    for i in range(len(my_list)):
        if my_list[i] % 2 > 0:
            my_list.insert(0, my_list.pop(i))
    return ''.join(str(e) for e in test_list)


# 38.写一个函数找出一个整数数组中，第二大的数
def find_second_large_num(num_list):
    return num_list.sort()[-2]


def find_second_large_num_1(num_list):
    top_1 = num_list[0]
    top_2 = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > top_1:
            top_2 = top_1
            top_1 = num_list[i]
        elif num_list[i] > top_2:
            top_2 = num_list[i]
    return top_2


# 39.阅读一下代码他们的输出结果是什么？
def multi():
    return [lambda x: i * x for i in range(4)]


def multi_1():
    result_list = []
    for i in range(4):
        def _lambda(x):
            return x * i

        result_list.append(_lambda)
    return result_list


# 40.统计一段字符串中字符出现的次数
def count_str(str_data):
    return collections.Counter(str_data)


def count_str_1(str_data):
    dict_str = {}
    for i in str_data:
        dict_str[i] = dict_str.get(i, 0) + 1
    return dict_str


# 41.super函数的具体用法和场景

"""
41.super函数的具体用法和场景
1. 单继承
在单继承时，super().__init__()与Base.__init__()是一样的。super()避免了基类的显式调用。

2. 多继承
super与父类没有实质性的关联。在单继承时，super获取的类刚好是父类，但多继承时，super获取的是继承顺序中的下一个类
如果不使用super，会导致基类被多次调用，开销非常大。
对于定义的类，在Python中会创建一个MRO(Method Resolution Order)列表，它代表了类继承的顺序。
查看MRO列表：MRO的查找顺序是按广度优先来的
"""

# 42.Python中类方法、类实例方法、静态方法有何区别？

"""
类方法就是类对象的方法，定义时加上@classmethod进行装饰，形参是cls，表示类对象。类对象和实例都可以调用
类实例方法是类实例化对象的方法，只有实例对象可以调用，形参为self 指代对象本身
静态方法 是任意函数 @staticmethod装饰。可以用对象直接使用 静态方法跟类没有太大关系
"""

# 介绍Cython，Pypy Cpython Numba各有什么缺点【面试题详解】
"""
Cython: Cython是Python的一个超集，结合了Python的易用性和原生代码的速度，可以编译成C语言。
PyPy: PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译
Jython: Jython是将Python code在JVM上面跑和调用java code的解释器。
"""

# 46.请描述抽象类和接口类的区别和联系
"""
抽象类：规定了一系列的方法，并且必须由继承类来实现。由于有抽象方法，所以抽象类不能被实例化
接口类：跟抽象类相似。接口里定义的方法由引用类实现
区别和关联：
1. 接口是抽象类的变体 接口里的方法都是抽象的 抽象类里可以有非抽象的方法。抽象类是声明方法的存在而不实现的类
2. 接口可以继承，抽象类不可以
3. 接口定义的方法都是声明么有实现，抽象类可以实现部分方法
4. 接口基本数据为static而抽象类不是
"""

# 47.Python中如何动态获取和设置对象的属性
# if hasattr(Parent,'x'):
#     print(getattr(Parent,'x'))
#     setattr(Parent, 'x',3)

# 48.哪些操作会导致Python内存溢出，怎么处理？
"""
1 内存中加载的数据量过于庞大 如一次从数据库取出过多数据；未做分页处理。
2 集合类中有对对象的引用，使用完后未清空，使得JVM不能回收。
3 代码中存在死循环或循环产生过多重复的对象实体。
4 使用的第三方软件中的BUG或者调用了C语言开发的底层模块中出现了内存泄露。
5 代码中有“引用循环”，并且被循环引用的对象定义了__del__方法，就会发生内存泄露。
为什么循环引用的对象定义了__del__方法后collect就不起作用了呢？
gc模块最常使用的方法就是gc.collect()方法，使用collect方法对循环引用的对象进行垃圾回收。
如果我们在类中重载了__del__方法。__del__方法定义了删除对象时除了释放内存空间以外的其他操作。解释器就不会释放内存
在这里，首先del语句出现时本身引用计数就不为0(因为有循环引用的存在)，

内存溢出的解决方案
第一步，修改JVM启动参数，直接增加内存(-Xms，-Xmx参数一定不要忘记加)
第二步，检查错误日志，查看“OutOfMemory”错误前是否有其 它异常或错误
第三步，对代码进行走查和分析，找出可能发生内存溢出的位置

重点排查以下几点：
检查对数据库查询中，是否有一次获得全部数据的查询。
检查代码中是否有死循环或递归调用。
检查是否有大循环重复产生新对象实体。
检查List、MAP等集合对象是否有使用完后，未清除的问题。List、MAP等集合对象会始终存有对对象的引用，使得这些对象不能被GC回收。
第四步，使用内存查看工具动态查看内存使用情况

内存泄漏和内存溢出的区别
内存溢出是指向JVM申请内存空间时没有足够的可用内存了，就会抛出OOM即内存溢出。
内存泄漏是指，向JVM申请了一块内存空间，使用完后没有释放，由于没有释放，这块内存区域其他类加载的时候无法申请，
"""

# 49.关于Python内存管理,下列说法错误的是
# A,变量不必事先声明
# B,变量无须先创建和赋值而直接使用
# C,变量无须指定类型
# D,可以使用del释放资源

# 50.Python的内存管理机制及调优手段？
"""
内存管理机制: 引用计数、垃圾回收、内存池引用计数：

引用计数是一种非常高效的内存管理手段，当一个Python对象被引用时其引用计数增加1
当其不再被一个变量引用时则计数减1,当引用计数等于0时对象被删除。弱引用不会增加引用计数
引用计数也是一种垃圾收集机制，而且也是一种最直观、最简单的垃圾收集技术。当Python的某个对象的引用计数降为0时，
说明没有任何引用指向该对象，该对象就成为要被回收的垃圾了。
"""

# 内存泄露是什么？如何避免？

"""
内存泄漏指由于疏忽或错误造成程序未能释放已经不再使用的内存
有__del__()函数的对象间的循环引用是导致内存泄露的主凶。
不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。
通过Python扩展模块gc 来查看不能回收的对象的详细信息。
可以通过 sys.getrefcount(obj) 来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露
"""

# 52.python常见的列表推导式？
# [表达式 for 变量 in 列表 if 条件]

# 53.简述read、readline、readlines的区别

"""
read                 读取整个文件
readline             读取下一行
readlines            读取整个文件到一个迭代器以供我们遍历
"""

# 54.什么是Hash（散列函数）？
"""
hash函数就是把任意长的输入字符串变化成固定长的输出字符串的一种函数。输出字符串的长度称为hash函数的位数。
散列（Hashing）通过散列函数将要检索的项与索引（散列，散列值）关联起来，生成一种便于搜索的数据结构
应用最为广泛的hash函数是SHA-1和MD5，大多是128位和更长
"""

# 55.python函数重载机制？
"""
Python函数特性上没有特别强调重载
功能相同的时候 同名函数 可以通过不同的参数类型 参数个数来区分
参数类型不同的情况 python形参本身就可以接受任何类型的参数 没必要形成不同的函数
参数个数的情况 可以用缺省函数 对缺少的参数设定为缺省函数就是很必要的
"""


# 57.手写一个判断时间的装饰器
class TimeException(Exception):
    def __init__(self, exception_info):
        super(TimeException, self).__init__()
        self.info = exception_info

    def __str__(self):
        return self.info


def time_check(func):
    def wrapper(*args, **kwargs):
        if datetime.datetime.now().year == 2020:
            func(*args, **kwargs)
        else:
            raise TimeException("Out of time")

    return wrapper()


# 59.编写函数的4个原则
"""
1.函数设计要尽量短小
2.函数声明要做到合理、简单、易于使用
3.函数参数设计应该考虑向下兼容
4.一个函数只做一件事情，尽量保证函数语句粒度的一致性
"""

# 60.函数调用参数的传递方式是值传递还是引用传递？
"""
Python的参数传递有：位置参数、默认参数、可变参数、关键字参数。
函数参数的传值到要分情况：
    不可变参数用值传递：像整数和字符串这样的不可变对象 是通过拷贝进行传递的
        因为你无论如何都不可能在原处改变不可变对象。
    可变参数是引用传递：比如像列表，字典这样的对象是通过引用传递、和C语言里面的用
        指针传递数组很相似，可变对象能在函数内部改变。
"""

# 61.如何在function里面设置一个全局变量
# globals() 返回包含当前作用域全局变量的字典。
# global变量设置使用全局变量


# 62.对缺省参数的理解？
"""
缺省参数指在调用函数的时候没有传入参数的情况下，调用默认的参数，
在调用函数的同时赋值时，所传入的参数会替代默认参数。
*args是不定长参数，它可以表示输入参数是不确定的，可以是任意多个。
**kwargs是关键字参数，赋值的时候是以键值对的方式，参数可以是任意多
对在定义函数的时候不确定会有多少参数会传入时，就可以使用两个参数
"""


# 64.带参数的装饰器
def new_func(func):
    def wrapper(username, password):
        if username == 'root' and password == '123':
            print("Login success")
            return func()
        else:
            print("Wrong")
            return

    return wrapper


def new_func_1(func):
    def wrapper(*parts):
        if parts:
            counts = len(parts)
            for part in parts:
                print(part, ' ', end='')
            return func()
        else:
            print("Fail")
            return func()

    return wrapper


# 65.为什么函数名字可以当做参数用
# Python中一切皆对象，函数名是函数在内存中的空间，也是一个对象

# 66 Python中pass语句的作用是什么？
# 在编写代码时只写框架思路，具体实现还未编写就可以用pass进行占位，
# 是程序不报错，不会进行任何操作。

# 67.有这样一段代码，print c会输出什么，为什么？
# a = 10
# b = 20
# c = [a]
# a = 15
# 答：10对于字符串，数字，传递是相应的值

# 69.map函数和reduce函数？
# map(lambda x: x*x, [1, 2, 3, 4])
# 使用 lambda# [1, 4, 9, 16]
# map将传入的函数依次作用到序列的每个元素
# reduce(lambda x, y: x*y, [1, 2, 3, 4])
# 相当于 ((1 * 2) * 3) * 4
# 但作用不同：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 24

# 70.回调函数，如何通信的
# 回调函数是把函数的指针(地址)作为参数传递给另一个函数，
# 将整个函数当作一个对象，赋值给调用的函数。

# 71.Python主要的内置数据类型都有哪些
# 内建类型：布尔类型，数字，字符串，元组, 集合, 列表，字典
# print(dir('a')) 内建方法

# 72.map(lambda x:x*x，[y for y in range(3)])的输出？
# list(map(lambda x: x*x, [0,1,2]))

# 73.hasattr() getattr() setattr() 函数使用详解？
"""
hasattr(object,name)函数:判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True，否则返回False。
getattr(object, name[,default])函数：获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选
setattr(object, name, values)函数：给对象的属性赋值，若属性不存在，先创建再赋值
"""

# 74.一句话解决阶乘函数？
# print(reduce(lambda x, y: x * y, range(1, 5)))

# 75.什么是lambda函数？有什么好处
"""
lambda函数是一个可以接收任意多个参数(包括可选参数)并且返回单个表达式值的函数
1.lambda函数比较轻便，很适合需要完成一项功能，但是此功能只在此一处使用，连名字都很随意的情况下
2.匿名函数，一般用来给filter，map这样的函数式编程服务
3.作为回调函数，传递给某些应用，比如消息处理
"""

# 76.递归函数停止的条件？
"""
递归的终止条件一般定义在递归函数内部，在递归调用前要做一个条件判断，根据判断的结果选择是继续调用自身，还是return返回终止递归
终止的条件：判断递归的次数是否达到某一限定值
          判断运算的结果是否达到某个范围等，根据设计的目的来选择
"""


# 77.下面这段代码的输出结果将是什么？请解释
# def multipliers():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in multipliers()])
"""
上述问题产生的原因是python闭包的延迟绑定。
这意味着内部函数被调用时，参数的值在闭包内进行查找。因此，当任何由multipliers()返回的函数被调用时,i的值将在附近的范围进行查找。
那时，不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3.
"""

# 78.什么是lambda函数？它有什么好处？写一个匿名函数求两个数的和
# lambda函数是匿名函数，使用lambda函数能创建小型匿名函数，这种函数得名于省略了用def声明函数的标准步骤
# f=lambda x,y:x+y
# f(1,2)

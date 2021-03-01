import os
import shutil
import sys
import time

"""
Python3中，range返回的是可迭代对象 而不是列表类型 输出不会返回列表
"""
xx = list(range(10))
print(xx)

"""
在方法内部修改全局变量
"""
a = 1


def update():
    global a
    a = 2


update()
print(a)

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
print(dic)

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


def get_file(path_original):
    paths = {}
    for root, dirs, files in os.walk(path_original):
        for file in files:
            full_path = os.path.join(root, file)
            modify_time = time.strftime('%Y-%m', time.localtime(os.stat(full_path).st_mtime))
            paths[full_path] = modify_time
    return paths


def move_org(path):
    f_path, f_name = os.path.split(path[0])
    folder_name = path[1]
    des_path = os.path.join(f_path, folder_name)

    if os.path.exists(des_path):
        shutil.move(path[0], des_path)
    else:
        os.mkdir(des_path)
        shutil.move(path[0], des_path)


def main():
    path_original = r"D:\Image"
    paths = get_file(path_original)
    for path in paths.items():
        move_org(path)


if __name__ == '__main__':
    main()

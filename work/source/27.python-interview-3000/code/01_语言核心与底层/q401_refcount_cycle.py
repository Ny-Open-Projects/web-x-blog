import gc
import sys

class Node:
    def __init__(self):
        self.peer = None

a, b = Node(), Node()
a.peer, b.peer = b, a           # 制造循环引用

# 单个对象的引用计数:循环前 a 被变量 a、b.peer 引用,共 2
print("refcount of a =", sys.getrefcount(a))   # 注意 getrefcount 自身会临时 +1

del a, b
print("gc.garbage before collect:", len(gc.garbage))
print("unreachable collected:", gc.collect())  # >0,循环垃圾在这里才被回收

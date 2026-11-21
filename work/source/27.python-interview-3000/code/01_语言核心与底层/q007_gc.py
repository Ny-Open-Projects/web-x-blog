import gc
import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

if __name__ == "__main__":
    gc.disable()   # 演示引用计数与分代回收分离
    a = Node("a")
    b = Node("b")
    a.partner = b
    b.partner = a  # 循环引用
    ref = weakref.ref(a)

    del a, b       # 引用计数不为零,因为互相持有
    print(ref() is not None)  # True,还活着

    gc.collect()   # 分代 GC 打破循环
    print(ref() is None)      # True,已被回收
    gc.enable()

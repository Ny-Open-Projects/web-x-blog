import gc

class Node:
    def __del__(self):
        print("finalizing", hex(id(self) & 0xFFFF))

a, b = Node(), Node()
a.peer, b.peer = b, a          # 循环引用 + 双方都有 __del__
del a, b

print("garbage list:", gc.garbage)
n = gc.collect()               # PEP 442 之前这里回收不了,现在可以
print("collected:", n, "| garbage now:", gc.garbage)

import ctypes
import sys
import tracemalloc

class Box:
    __slots__ = ("v",)
    def __init__(self, v):
        self.v = v

print("refcnt offset layout (CTypes 只读观察):")
raw = ctypes.cast(id(1), ctypes.POINTER(ctypes.c_ssize_t))
print("head value of small int 1:", raw[0])       # 3.12+(PEP 683)不朽对象此值是标记值;3.12 前是普通 refcnt(小整数被大量引用,同样很大)
print("type ptr equal to int type:", ctypes.cast(id(1), ctypes.POINTER(ctypes.c_void_p))[1] == id(int))

print("getsizeof:", sys.getsizeof([]), sys.getsizeof([None]),
      "list 过度分配:", sys.getsizeof([None] * 100))
tracemalloc.start()
data = [Box(i) for i in range(100_000)]
print("tracemalloc total MB:", round(tracemalloc.get_traced_memory()[0] / 2**20, 1))
print("getsizeof 不会告诉你元素成本")

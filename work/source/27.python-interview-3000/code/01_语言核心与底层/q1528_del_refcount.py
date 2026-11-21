import gc
import sys
import weakref


class Blob:
    def __init__(self, payload):
        self.payload = payload


class Node:
    def __init__(self):
        self.partner = None


if __name__ == "__main__":
    big = Blob([0] * 1000)
    ref = weakref.ref(big)
    gone = weakref.finalize(big, print, "finalize: big 被回收")
    print("alive before del:", ref() is not None)
    del big                        # 解绑最后一个引用,计数归零立即回收
    print("alive after  del:", ref() is not None)
    del gone                       # 终结器随主体死亡已触发,主动解除

    # 循环引用:del 掉外部名字不会立即回收,需要 gc 介入
    a, b = Node(), Node()
    a.partner, b.partner = b, a
    ra = weakref.ref(a)
    del a, b
    print("cycle alive before gc:", ra() is not None)
    gc.collect()
    print("cycle alive after  gc:", ra() is not None)

    # del 切片清内容 vs del 名字:别名视角完全不同
    buf = list(range(10))
    alias = buf
    del buf[:]                     # 清内容:alias 同步变空
    print("after del buf[:]: alias =", alias)
    del alias                      # 只删名字:列表对象因无引用而回收

    # getrefcount 的临时参数引用:恒比真实引用数多 1
    s = "x" * 3
    print("getrefcount(s):", sys.getrefcount(s), " 含传入的临时引用")

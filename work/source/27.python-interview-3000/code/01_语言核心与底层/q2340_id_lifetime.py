"""id() 的生命周期陷阱:表达式结束后对象即可回收,地址可被复用。"""
import gc
import weakref


class Box:
    def __init__(self, tag):
        self.tag = tag


if __name__ == "__main__":
    id1 = id(Box("a"))
    id2 = id(Box("b"))
    print("两个临时对象的 id 相等:", id1 == id2)   # 地址复用,True 但无意义

    x = Box("keep")
    y = x
    print("同时存活的别名 is 判断可靠:", x is y)

    b1 = Box("first")
    b2 = Box("second")
    print("持有引用后 id 必不相同:", id(b1) != id(b2))

    cache = weakref.WeakValueDictionary()
    cache["first"] = b1
    print("弱引用取回同一对象:", cache["first"] is b1)
    del b1
    gc.collect()
    print("引用消失后弱引用自动清理:", "first" not in cache)

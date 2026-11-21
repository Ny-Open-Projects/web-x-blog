"""weakref 实现的弱缓存:对象回收后缓存自动清理。"""
import gc
import weakref


class Expensive:
    def __init__(self, name):
        self.name = name


cache = weakref.WeakValueDictionary()


def get_expensive(name):
    obj = cache.get(name)
    if obj is None:
        print(f"重建 {name}")
        obj = Expensive(name)
        cache[name] = obj  # 只存弱引用
    else:
        print(f"命中缓存 {name}")
    return obj


if __name__ == "__main__":
    a = get_expensive("conn-1")   # 重建
    b = get_expensive("conn-1")   # 命中
    print("同一对象:", a is b)
    print("当前缓存键:", list(cache.keys()))

    del a, b
    gc.collect()                  # 外部引用消失,对象被回收
    print("回收后缓存键:", list(cache.keys()), "<- 自动清理, 无泄漏")
    get_expensive("conn-1")       # 重新重建

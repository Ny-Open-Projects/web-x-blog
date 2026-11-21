"""弱引用容器:缓存、元数据挂载与实例追踪三种场景。"""
import gc
import weakref


class Report:
    def __init__(self, rid):
        self.rid = rid


def value_cache_demo():
    cache = weakref.WeakValueDictionary()
    r1 = Report(1)               # 先持强引用
    cache["r1"] = r1             # 值侧是弱引用
    print("  放入后:", len(cache))
    del r1
    gc.collect()                 # 唯一强引用消失,条目自动移除
    print("  对象回收后:", len(cache))


def key_meta_demo():
    meta = weakref.WeakKeyDictionary()
    doc = Report(2)
    meta[doc] = {"last_open": "2026-01-01"}   # 键侧是弱引用
    print("  挂载元数据:", meta[doc])
    del doc
    gc.collect()
    print("  键销毁后:", len(meta))


def instance_tracking_demo():
    seen = weakref.WeakSet()

    class Node:
        def __init__(self):
            seen.add(self)

    a, b = Node(), Node()
    print("  存活实例数:", len(seen))
    del a, b
    gc.collect()
    print("  全部回收后:", len(seen))


if __name__ == "__main__":
    print("WeakValueDictionary 充当自动过期的缓存:")
    value_cache_demo()
    print("WeakKeyDictionary 给对象挂外挂元数据:")
    key_meta_demo()
    print("WeakSet 追踪存活实例:")
    instance_tracking_demo()

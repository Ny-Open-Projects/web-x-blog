import weakref

class Heavy:
    def __init__(self, name):
        self.name = name

cache = weakref.WeakValueDictionary()   # 值是弱引用

obj = Heavy("model")
cache["model"] = obj                    # 缓存不阻止回收
print("hit:", cache.get("model").name)

del obj                                 # 强引用消失
print("after del, hit:", cache.get("model"))   # None,条目自动蒸发

# 观察者模式:发布者不延长监听器生命周期
class Publisher:
    def __init__(self):
        self.listeners = weakref.WeakSet()
    def notify(self):
        for l in list(self.listeners):
            print("notify", l.name)

pub = Publisher()
listener = Heavy("listener")
pub.listeners.add(listener)
pub.notify()
del listener                            # 监听器可被独立回收

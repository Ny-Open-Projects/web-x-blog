import time

class cached_property:
    """惰性计算 + 缓存 + 可手动失效"""
    def __init__(self, func):
        self.func = func
        self.attr = func.__name__
        self.__doc__ = func.__doc__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        cache = obj.__dict__
        if self.attr not in cache:
            cache[self.attr] = self.func(obj)   # 首次访问才计算
        return cache[self.attr]

    def invalidate(self, obj):
        obj.__dict__.pop(self.attr, None)

class Report:
    def __init__(self, data):
        self.data = data
        self.loads = 0

    @cached_property
    def stats(self):
        self.loads += 1
        time.sleep(0.01)                    # 模拟昂贵计算
        return {"sum": sum(self.data), "n": len(self.data)}

if __name__ == "__main__":
    r = Report([1, 2, 3, 4])
    print(r.stats)                          # 计算一次
    print(r.stats)                          # 直接读实例字典缓存
    print("computed:", r.loads, "times")
    Report.stats.invalidate(r)              # 类访问拿描述符,再对实例失效
    print(r.stats)                          # 重新计算
    print("computed:", r.loads, "times")

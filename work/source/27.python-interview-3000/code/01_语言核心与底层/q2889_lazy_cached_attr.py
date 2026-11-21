"""惰性求值的属性缓存:手写可失效的缓存属性与 cached_property 对比。"""
import functools


class Report:
    """手写版:显式缓存槽 + invalidate 方法,失效时机自己掌控。"""

    def __init__(self, rows):
        self.rows = rows
        self._stats = None

    @property
    def stats(self):
        if self._stats is None:
            print("  -> Report 计算一次")
            total = sum(self.rows)
            self._stats = {"total": total, "mean": total / len(self.rows)}
        return self._stats

    def invalidate(self):
        self._stats = None


class Dataset:
    """cached_property 版:缓存藏在实例 __dict__,删除键即失效。"""

    def __init__(self, rows):
        self.rows = rows

    @functools.cached_property
    def summary(self):
        print("  -> Dataset 计算一次")
        return {"total": sum(self.rows), "count": len(self.rows)}


if __name__ == "__main__":
    r = Report([3, 1, 2])
    print(r.stats)
    print(r.stats)                 # 第二次读缓存,不再打印计算
    r.rows.append(100)
    r.invalidate()
    print("失效后重算:", r.stats)

    d = Dataset([1, 2, 3])
    print(d.summary)
    print("缓存在实例字典里:", "summary" in vars(d))
    del d.summary                  # 删除键即失效,下次访问重算
    print("删除键后重算:", d.summary)

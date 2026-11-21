import tracemalloc


class Cache:
    # 无界缓存:内存泄漏的典型形态
    def __init__(self):
        self._data = {}

    def put(self, key, value):
        self._data[key] = value


def leak_simulation():
    tracemalloc.start()
    cache = Cache()
    before = tracemalloc.take_snapshot()
    for i in range(10_000):
        cache.put(f"key-{i}", "x" * 64)
    after = tracemalloc.take_snapshot()
    stats = after.compare_to(before, "lineno")
    top = stats[0]
    tracemalloc.stop()
    return top.size_diff


def test_detect_growth():
    growth = leak_simulation()
    # 检测到明显增长,证明定位到了泄漏点
    assert growth > 10_000

"""pytest 完整测试类示例: 夹具 + 参数化 + 异常断言; 无 pytest 环境用内置 runner 走同一套断言"""
try:
    import pytest
except ImportError:
    pytest = None


class TinyKV:
    """被测对象: 容量受限的 KV 存储, 超容 RuntimeError, 取缺失 KeyError"""
    def __init__(self, capacity=3):
        self.capacity = capacity
        self._data = {}

    def set(self, key, value):
        if key not in self._data and len(self._data) >= self.capacity:
            raise RuntimeError("容量已满, 上限 %d" % self.capacity)
        self._data[key] = value

    def get(self, key):
        if key not in self._data:
            raise KeyError(key)
        return self._data[key]

    def clear(self):
        self._data.clear()


if pytest is not None:
    @pytest.fixture()
    def kv():
        """夹具: 每个测试拿到带种子数据的新实例, 结束后自动清理"""
        store = TinyKV(capacity=3)
        store.set("a", 1)
        yield store
        store.clear()

    class TestTinyKV:
        def test_seed_value_visible(self, kv):
            assert kv.get("a") == 1

        @pytest.mark.parametrize("k,v", [("b", 2), ("c", 3)])
        def test_set_then_get(self, kv, k, v):
            kv.set(k, v)
            assert kv.get(k) == v

        def test_get_missing_raises(self, kv):
            with pytest.raises(KeyError):
                kv.get("zz")

        def test_overflow_raises(self, kv):
            kv.set("b", 2)
            kv.set("c", 3)
            with pytest.raises(RuntimeError):
                kv.set("d", 4)

else:
    def expect_raises(exc_type, fn):
        try:
            fn()
        except exc_type:
            return
        raise AssertionError("期望抛出 %s 但未抛出" % exc_type.__name__)

    def run_fallback():
        """降级 runner: 手工搭建同样的夹具语义, 逐条复现测试断言"""
        results = []

        def run(name, fn):
            try:
                fn()
                results.append((name, "PASS"))
            except Exception as e:
                results.append((name, "FAIL: %s" % e))

        def fresh():
            s = TinyKV(capacity=3)
            s.set("a", 1)
            return s

        def test_seed_value_visible():
            s = fresh()
            assert s.get("a") == 1
            s.clear()

        def test_set_then_get():
            for k, v in (("b", 2), ("c", 3)):      # 等价于参数化两组用例
                s = fresh()
                s.set(k, v)
                assert s.get(k) == v
                s.clear()

        def test_get_missing_raises():
            s = fresh()
            expect_raises(KeyError, lambda: s.get("zz"))
            s.clear()

        def test_overflow_raises():
            s = fresh()
            s.set("b", 2)
            s.set("c", 3)
            expect_raises(RuntimeError, lambda: s.set("d", 4))
            s.clear()

        for t in (test_seed_value_visible, test_set_then_get,
                  test_get_missing_raises, test_overflow_raises):
            run(t.__name__, t)
        return results


if __name__ == "__main__":
    if pytest is not None:
        sys_exit = __import__("sys").exit
        sys_exit(pytest.main([__file__, "-q"]))
    print("pytest 未安装, 内置降级 runner:")
    failed = 0
    for name, status in run_fallback():
        print("  %-24s %s" % (name, status))
        if status != "PASS":
            failed += 1
    print("共 %d 例, 失败 %d 例" % (4, failed))
    raise SystemExit(1 if failed else 0)

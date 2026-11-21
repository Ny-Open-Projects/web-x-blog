---
title: [Q2970] pytest 完整测试类示例:夹具+参数化+异常断言
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2970 · pytest 完整测试类示例:夹具+参数化+异常断言

> 难度:★★★☆ | 标签:pytest, 单元测试

**问**:面试官:现场写一个测试类,把夹具、参数化、异常断言完整串起来。

**答**:被测对象 TinyKV:容量 3 的 KV 存储,超容抛 RuntimeError,取缺失抛 KeyError。夹具 kv 负责搭种子数据并在 yield 后清理,每个测试拿到全新实例互不污染。参数化 test_set_then_get 覆盖两组用例 b 为 2、c 为 3;异常断言用 pytest.raises 分别验证 KeyError 与容量满的 RuntimeError。共 4 个测试方法;本机没有 pytest 时内置降级 runner 复现同一套断言,4 例全部 PASS;有 pytest 时同一文件可被直接收集。这套组合覆盖了单测 80% 的日常场景:状态准备、多组输入、异常路径。

```python
# file: code/05_数据分析与工程化/q2970_pytest_demo.py
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
```

**追问**:
- 追问 1:夹具比 setUp 好在哪?—— 依赖注入、可嵌套、可指定 scope,多个夹具组合不需要继承链。
- 追问 2:参数化用例失败怎么定位?—— pytest 把每组参数当独立用例,用例 ID 可读,失败哪组一目了然。

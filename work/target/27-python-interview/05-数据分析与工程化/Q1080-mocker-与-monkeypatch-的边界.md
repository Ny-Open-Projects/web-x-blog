---
title: [Q1080] mocker 与 monkeypatch 的边界
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1080 · mocker 与 monkeypatch 的边界

> 难度:★★★☆ | 标签:pytest, mock

**问**:pytest 自带 monkeypatch,为什么还有人装 pytest-mock 的 mocker?两者怎么选?

**答**:monkeypatch 是基础工具: setattr/delitem/patch.dict,改属性、改环境变量、改 cwd,退出自动还原,胜在零依赖直接。mocker 是 unittest.mock 的 fixture 化包装,强项是 mock 语义:patch 后拿到 Mock 对象,能断言 `assert_called_once_with`、控制 return_value/side_effect,还能用 `spy` 包装真函数记录调用。选型口诀:换行为、改环境用 monkeypatch;要验证"有没有被调用、用什么参数调用"的交互行为用 mocker。别混用两层导致还原顺序混乱。

```python
# file: code/05_数据分析与工程化/q1080_mocker_boundary.py

class PriceClient:
    def get_price(self, sku):
        raise RuntimeError("真实网络调用")

def total_price(client, items):
    return sum(client.get_price(sku) * qty for sku, qty in items)

class MonkeyPatch:
    """模拟 pytest 的 monkeypatch:退出自动还原"""

    def __init__(self):
        self._undo = []

    def setattr(self, obj, name, value):
        old = getattr(obj, name)
        setattr(obj, name, value)
        self._undo.append(lambda: setattr(obj, name, old))

    def undo(self):
        for fn in reversed(self._undo):
            fn()

class SpyClient:
    """spy 记录调用,供交互断言,mocker 的典型用法"""

    def __init__(self):
        self.calls = []

    def get_price(self, sku):
        self.calls.append(sku)
        return 100

if __name__ == "__main__":
    items = [("A", 2), ("B", 1)]
    patch = MonkeyPatch()
    patch.setattr(PriceClient, "get_price", lambda self, sku: 10)
    assert total_price(PriceClient(), items) == 30
    patch.undo()
    spy = SpyClient()
    total_price(spy, items)
    assert spy.calls == ["A", "B"]
    print("monkeypatch 换行为,spy/mocker 验证交互,边界清晰")
```

**追问**:
- 追问 1:patch 位置坑在 mocker 下也存在吗?—— 存在,mocker.patch("模块.名字") 同样要 patch 使用处而非定义处,原理一致。
- 追问 2:monkeypatch 改了模块级常量影响别的测试吗?—— 不会,fixture 结束自动还原;但多线程共享状态下要小心竞态。

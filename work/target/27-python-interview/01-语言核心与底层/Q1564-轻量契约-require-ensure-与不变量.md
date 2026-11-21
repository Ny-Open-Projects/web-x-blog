---
title: [Q1564] 轻量契约:require、ensure 与不变量
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1564 · 轻量契约:require、ensure 与不变量

> 难度:★★★★☆ | 标签:契约, 不变量, 防御式编程

**问**:不引入重型库,怎么给函数加前置条件、后置条件?断言做契约有什么致命局限?

**答**:轻量契约的最小实现是三个 helper:require(前置——违反即调用方 bug,抛 ValueError)、ensure(后置——违反即实现者 bug,抛 RuntimeError)、不变量(状态转换后检查,如「转账不创造金额」「余额非负」)。与 assert 的区别是生存性:assert 在 -O 下整体消失(Q470),承载不了运行时契约;helper 是真实函数,任何模式都在场。要点:① 失败类型分层让「谁修」一目了然:ValueError 调用方修,RuntimeError 实现修;② 契约只挂公共边界与状态转换点,内部路径零契约,热点可加 debug 开关;③ dataclass 的 __post_init__ 是后置条件天然挂点;④ 契约消息要写成「违反了什么承诺」,不是「发生了什么」。

```python
# file: code/01_语言核心与底层/q1564_lightweight_contract.py


def require(condition, message):
    """前置条件:违反 = 调用方的 bug,ValueError。"""
    if not condition:
        raise ValueError(message)


def ensure(condition, message):
    """后置条件:违反 = 实现者的 bug,RuntimeError。"""
    if not condition:
        raise RuntimeError("internal invariant broken: " + message)


class Ledger:
    def __init__(self, balances):
        self.balances = dict(balances)
        self._check_invariant()

    def _check_invariant(self):
        ensure(all(v >= 0 for v in self.balances.values()), "余额不得为负")
        ensure(set(self.balances) == {"alice", "bob"}, "账户集合固定")

    def transfer(self, src, dst, amount):
        require(amount > 0, "amount 必须为正, got %s" % amount)
        require(src in self.balances and dst in self.balances,
                "账户必须存在, got %r/%r" % (src, dst))
        before = sum(self.balances.values())
        self.balances[src] -= amount
        self.balances[dst] += amount
        self._check_invariant()                  # 状态转换后的不变量
        ensure(sum(self.balances.values()) == before, "转账不得创造或销毁金额")
        return self.balances[src], self.balances[dst]


if __name__ == "__main__":
    ledger = Ledger({"alice": 100, "bob": 50})
    print("transfer 30:", ledger.transfer("alice", "bob", 30))
    print("balances   :", ledger.balances)

    for bad in [("alice", "bob", 0), ("ghost", "bob", 5), ("alice", "bob", 999)]:
        try:
            ledger.transfer(*bad)
        except (ValueError, RuntimeError) as err:
            print("%s: %s" % (type(err).__name__, err))

    print("total intact:", sum(ledger.balances.values()) == 150)
```

**追问**:1) 契约检查的性能代价怎么控?——只挂公共边界与状态转换点,内部路径零契约;热点路径可加 debug 开关聚合关闭。2) require/ensure 的设计要点?——前置条件(require)在入口、后置条件(ensure)在出口、不变量(invariant)在状态转换后;失败抛专用 ContractError(不可剥离,区别于 assert);消息带上完整上下文。3) 与类型系统的分工?——静态层(mypy/pyright)管类型契约,运行时契约管值域与状态;两者重叠面越少越好,运行时只兜「静态表达不了」的约束。4) 生产陷阱?——契约写进 assert 被 -O 剥离(Q470);契约内部再调契约递归触发;把契约当校验用(重复检查掩盖 bug,Q1278)。

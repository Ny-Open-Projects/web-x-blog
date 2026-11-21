---
title: [Q7066] pytest fixture 作用域与状态泄漏
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7066 · pytest fixture 作用域与状态泄漏

难度：P6 | 标签：pytest、fixture、测试隔离、事故复盘

**问**：测试单跑全过、全量跑随机挂，这类"测试顺序依赖"的根因是什么？fixture 的 function/session 作用域怎么选？怎么系统性治理状态泄漏？

**答**：
- **结论**：根因是跨测试共享可变状态：module/session 级 fixture 的对象被多个测试复用，谁改了它谁就污染别人；加上 pytest-xdist 并行后，全局资源（环境变量、临时目录、数据库表）的竞争进一步放大。选作用域的原则：只读且创建昂贵的资源用 session 级（启动容器、加载模型）；任何会被测试写入的对象必须 function 级，或配套 autouse 的重置 fixture。
- **取舍**：session 级 + 每测重置（快）vs function 级重建（慢但天然隔离）。数据库类测试用"事务回滚"方案：session fixture 建连接，function fixture 开事务、测完 rollback，兼得隔离与速度；代价是测试代码必须走同一连接，且被测代码内部不能自己 commit。
- **实战**：治理三板斧：① 上 pytest-randomly 打乱顺序，把顺序依赖逼出来；② monkeypatch/tmp_path 管理一切外部状态，禁止测试直接改全局；③ CI 里开 xdist 分片，让"隐式共享"无处藏身。修复后用"两两组合跑"验证顺序无关性。

```python
"""pytest fixture 作用域与状态泄漏。运行：python3 本文件（内部调 pytest.main）"""
import pytest

class Store:
    def __init__(self):
        self.items = {}
    def add(self, k):
        self.items[k] = True

@pytest.fixture(scope="module")
def shared_store():                 # module 级：整个模块共用一个实例
    return Store()

@pytest.fixture()
def fresh_store():                  # function 级：每测重建，天然隔离
    return Store()

def test_a(shared_store, fresh_store):
    shared_store.add("a")           # 污染共享 fixture
    fresh_store.add("a")
    assert list(fresh_store.items) == ["a"]

def test_b(shared_store, fresh_store):
    assert fresh_store.items == {}                  # 通过：function 级隔离
    assert "a" in shared_store.items               # 证明：module 级状态泄漏了

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
```

**追问链**：
1. 追问一层：fixture 的 teardown 在 yield 之后，什么时候会不被执行？——setup 抛异常则 teardown 不跑；session 级 fixture 在进程被 kill 时也不跑，所以临时资源要有兜底清理（如 tmp_path 自带过期清理）。
2. 追问二层：xdist 下 session 级 fixture 是每个 worker 各建一份，这带来什么问题？——每个 worker 独立建容器/连接，资源翻倍；跨 worker 共享要靠文件锁或外部预建服务，不能想当然以为"session=全局一份"。

**背诵要点**：
1. 顺序依赖根因是跨测试可变状态；用 pytest-randomly 逼出依赖。
2. 昂贵只读资源用 session，可变对象必须 function 级或配套重置。
3. DB 测试用事务回滚方案兼顾隔离与速度。

**复盘追问**：
1. 全量跑挂、单跑过的用例，为什么"加 time.sleep 修复"是错误做法？（掩盖资源竞争时序，正确做法是定位共享状态）
2. session fixture 里建了 DB 连接但某用例把连接关闭了，下游用例会怎样？（连接失效报错，说明资源归还策略也要纳入 fixture 管理）

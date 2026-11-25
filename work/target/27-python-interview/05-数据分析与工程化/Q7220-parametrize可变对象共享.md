---
title: "[Q7220] parametrize 传了同一个 list：用例为什么会互相污染"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7220 · parametrize 传了同一个 list：用例为什么会互相污染

难度：P6 ｜ 标签：pytest、parametrize、可变对象、测试隔离

基线：Python 3.12；pytest 7/8 `@pytest.mark.parametrize`；纯 Python 模拟收集与执行。

**问**：参数化写了 `@pytest.mark.parametrize("bucket", [[], []])`，两个用例都是"往 bucket 里加一个元素，断言长度 1"。单独跑都过，一起跑第二个必挂；换 `-p no:randomly` 顺序又变了。两个空列表看起来是两个参数，为什么实际是同一个对象？还有哪些同类坑？

**答**：
- **结论**：`parametrize` 的参数在**收集阶段求值一次**，之后每个用例拿到的是同一个对象引用。`[[], []]` 里的两个 list 字面量其实是**两个不同对象**，这个例子本身不会共享——真正会共享的是：① 先定义 `BASE = []` 再 `parametrize("x", [BASE, BASE])`；② 参数是模块级 dict/list 被引用；③ 用 `pytest.fixture(params=[...])` 时 params 里的可变对象被多个用例复用。一旦用例修改参数对象，后续用例看到脏状态，表现为**顺序依赖的 flaky**。
- **取舍**：参数化适合"不可变输入"（数字、字符串、tuple、frozen dataclass）；可变输入要么用**工厂函数**（每个用例调用一次生成新对象），要么在 fixture 里做深拷贝，要么把"构造"和"断言"分离。给每个参数加 `ids=` 能提高可读性，但 id 不解决共享问题。
- **实战**：① 参数用 `lambda: []` / `functools.partial` 这类工厂，用例内调用；② 必须在参数里放可变对象时，在用例开头 `copy.deepcopy`；③ 用 `pytest-randomly` 打乱顺序跑一遍，暴露顺序依赖；④ 断言前先断言"输入是干净的"（长度/内容），把污染变成显式失败而不是玄学。

```python
"""模拟 parametrize 的收集/执行：同一个可变对象被多个用例复用。"""
import copy
from typing import Callable


def parametrize(values: list) -> Callable:
    def deco(fn: Callable) -> Callable:
        fn.params = values          # 收集阶段一次性绑定
        return fn
    return deco


def run(fn: Callable) -> list[str]:
    results = []
    for i, value in enumerate(fn.params):
        try:
            fn(value)
            results.append(f"case{i}: PASS")
        except AssertionError as e:
            results.append(f"case{i}: FAIL ({e})")
    return results


SHARED: list[int] = []


@parametrize([SHARED, SHARED])       # 同一个 list 被引用两次
def test_shared(bucket: list[int]) -> None:
    bucket.append(1)
    assert len(bucket) == 1, f"bucket 被污染，长度={len(bucket)}"


@parametrize([lambda: [], lambda: []])   # 工厂：每次生成新对象
def test_factory(make_bucket) -> None:
    bucket = make_bucket()
    bucket.append(1)
    assert len(bucket) == 1


@parametrize([{"tags": []}, {"tags": []}])
def test_deepcopy(payload: dict) -> None:
    local = copy.deepcopy(payload)      # 用例内隔离
    local["tags"].append("x")
    assert len(payload["tags"]) == 0


if __name__ == "__main__":
    print("共享可变对象:", run(test_shared))
    print("工厂函数    :", run(test_factory))
    print("深拷贝      :", run(test_deepcopy))
    print("结论：参数在收集期求值；可变输入要用工厂或 deepcopy")
```

**追问一**：为什么 `pytest-xdist` 下这类污染有时反而"消失"了？
→ 解析：xdist 把用例分发到不同 worker 进程，每个进程有独立的内存空间，模块级可变对象不共享，污染被"进程隔离"掩盖。但同一 worker 内仍可能复现，且 `--dist loadscope`/`loadfile` 的分组方式会改变顺序，导致"本地挂、CI 过"或反之。不能靠 xdist 掩盖隔离缺陷。

**追问二**：`parametrize` 的 `ids` 和 `indirect` 分别解决什么问题？
→ 解析：`ids` 只影响用例显示名与报告可读性，不改变对象身份；`indirect=True` 表示参数不直接传给测试函数，而是传给同名 fixture，由 fixture 做构造/清理——这才适合需要 setup/teardown 或每例独立资源的参数化。可变资源应优先走 `indirect` + fixture，而不是直接塞对象。

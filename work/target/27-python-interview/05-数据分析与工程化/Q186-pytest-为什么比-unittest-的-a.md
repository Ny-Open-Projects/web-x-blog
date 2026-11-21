---
title: [Q186] pytest 为什么比 unittest 的 assert 更好用
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q186 · pytest 为什么比 unittest 的 assert 更好用

> 难度:★☆☆ | 标签:pytest, assert

**问**:pytest 直接写裸 assert 就能给出详细失败信息,unittest 却要记一堆 assertEqual 方法,这是怎么做到的?

**答**:pytest 对测试文件做了 **assertion rewriting**:在导入时(pytest 启动阶段,通过 import hook)把模块里的 `assert` 语句重写为中间表示,失败时把左右表达式的值、比较运算都展示出来。所以你写普通 assert,却能获得 `assert 1 == 2` 加上 `E + where 1 = f()` 这样的详细 diff。相比 unittest 的好处是:无样板类继承、无记忆负担、失败信息更可读。原生 assert 在被 `python -O` 运行时会被整体移除,这是裸 assert 的经典坑。

```python
# file: code/05_数据分析与工程化/q186_pytest_assert.py
def add(a, b):
    return a + b

def test_add():
    # 裸 assert 即可,失败时 pytest 会展示 add(1, 2) 的实际值
    assert add(1, 2) == 3

def test_add_negative():
    result = add(-1, -2)
    # 失败时输出类似: assert -3 == -4  where -3 = add(-1, -2)
    assert result == -4

if __name__ == "__main__":
    # 手动验证:用 python -m pytest 运行本文件
    import subprocess, sys
    print("请用: python -m pytest q186_pytest_assert.py 运行")
```

**追问**:
- `python -O` 会怎样?——它会删除所有 assert 语句,测试将静默通过,所以跑测试永远不要带 -O。
- assertion rewriting 是什么时候发生的?——import hook 在收集导入阶段改写,所以pytest 外直接跑脚本没有增强输出。
- unittest 还值得用吗?——遗留代码与团队既有约定;新项目统一 pytest,二者可共存(pytest 能跑 unittest 用例)。
- assert 写法有什么禁忌?——别把「验证行为」写成恒真式(assert list);多条件拆成多行 assert,失败信息才精确。

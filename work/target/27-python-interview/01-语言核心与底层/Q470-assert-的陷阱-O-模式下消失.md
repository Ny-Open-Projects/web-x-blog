---
title: [Q470] assert 的陷阱:-O 模式下消失
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q470 · assert 的陷阱:-O 模式下消失

> 难度:★★★☆ | 标签:assert, 异常

**问**:为什么「用 assert 做参数校验」是生产事故的高发原因?

**答**:assert 语句依赖内置变量 __debug__:python -O 启动时 __debug__ 为 False,所有 assert 连同消息表达式一起被剥离,字节码里根本不存在。于是「assert amount > 0」这类校验在优化模式下静默失效,负数长驱直入。分工原则:assert 表达「此处不变式必须为真」,用于内部自检、测试断言、以及「如果这里不成立就是 bug」的场景;对外部输入与业务规则一律 raise,或交给显式校验层。消息表达式里放副作用(如计数器)同样会在 -O 下消失,也是坑。

```python
# file: code/01_语言核心与底层/q470_assert_pitfall.py
def withdraw(balance: int, amount: int) -> int:
    assert amount > 0, "amount must be positive"    # python -O 下被剥离
    if amount > balance:
        raise ValueError("insufficient funds")      # 业务规则必须用异常
    return balance - amount

if __name__ == "__main__":
    print(withdraw(100, 30))
    print("assertions enabled:", __debug__)
    try:
        withdraw(100, -1)
    except AssertionError as e:
        print("assert fired:", e)
    print("with -O the assert vanishes and -1 passes the first check")
```

**追问**:1) pytest 的 assert 增强(-O 冲突吗)?——pytest 重写 assert 字节码生成详细失败信息,要求测试不以 -O 运行;CI 里区分「应用 -O 提速」与「测试全量断言」两套配置。2) -O 到底剥掉什么?——-O 置 __debug__=False 且编译期剥离 assert(连同消息表达式);-OO 连 docstring 一起剥,影响 doctest 与按文档字符串的反射工具。3) 剥离发生在哪个阶段?——编译期:assert 语句不生成字节码,不是运行时判断 __debug__ 分支;消息里的副作用(计数器、logging)在 -O 下静默消失,这是「assert 里带副作用」被禁的根因。4) 生产陷阱?——生产环境误配 PYTHONOPTIMIZE,参数校验全灭是真实事故模式;部署镜像与 CI 的解释器参数要对齐,业务校验永不写 assert。

---
title: [Q1542] Decimal 上下文:精度与舍入的主人
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1542 · Decimal 上下文:精度与舍入的主人

> 难度:★★★★☆ | 标签:decimal, 精度, 上下文

**问**:Decimal("1") + Decimal("1.0") 的精度谁说了算?为什么同样的除法在不同线程结果可能不同?

**答**:Decimal 运算的精度与舍入由「当前上下文」决定,不由数字本身:decimal.getcontext() 是线程本地的 Context(prec=28、rounding=ROUND_HALF_EVEN、traps 等),所有算术结果按它舍入(Q538 讲货币工程,本题讲上下文机制)。要点:① Decimal(str) 构造是精确的,上下文只在运算结果上生效——两个长数字相乘会被削到 prec 位;② 局部改精度用 with localcontext(),退出自动还原;全局 setcontext 改了不还原是事故源;③ 上下文线程本地——主线程改 prec 不影响子线程,「同式不同果」的根源在这里;④ traps 决定哪些条件升级为异常,除零默认抛 DivisionByZero 而不是返回 Infinity;⑤ 展示层用 quantize(Decimal("0.01"), rounding=...) 显式定舍入,与 prec 配合防 InvalidOperation。

```python
# file: code/01_语言核心与底层/q1542_decimal_context.py
import threading
from decimal import (Decimal, DivisionByZero, ROUND_HALF_UP, getcontext,
                     localcontext)


def multiply_wide():
    a = Decimal("1." + "2" * 30)       # 31 位有效数字,精确构造
    b = Decimal("3")
    return a * b                        # 结果按当前上下文 prec 舍入


if __name__ == "__main__":
    ctx = getcontext()
    print("default prec:", ctx.prec, "| rounding:", ctx.rounding)
    print("prec=31 mult:", multiply_wide())

    with localcontext() as local:
        local.prec = 6
        print("prec=6  mult:", multiply_wide())
        print("1/3 at prec 6:", Decimal(1) / Decimal(3))
    print("restored prec:", getcontext().prec == ctx.prec)

    # 线程本地:子线程改 prec,主线程不受影响
    results = {}

    def worker():
        getcontext().prec = 4
        results["worker"] = str(Decimal(1) / Decimal(3))
        results["worker_prec"] = getcontext().prec

    t = threading.Thread(target=worker)
    t.start()
    t.join()
    print("worker:", results["worker"], "prec:", results["worker_prec"])
    print("main prec still:", getcontext().prec)

    # 量化到分:显式舍入模式,展示层专用
    price = Decimal("19.985")
    print("half_up  :", price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    print("default  :", price.quantize(Decimal("0.01")), " 上下文 half-even")

    # traps:除零默认升级为异常,而不是返回 Infinity
    try:
        Decimal(1) / Decimal(0)
    except DivisionByZero:
        print("division by zero -> DivisionByZero")
```

**追问**:1) quantize 的精度不够会怎样?——结果超过上下文 prec 时抛 InvalidOperation;先确保 prec 覆盖量化后位数,或临时 localcontext 提精度。2) context 控制什么?——prec 有效位数、rounding 舍入模式、Emin/Emax 指数范围;所有算术按当前上下文舍入——「Decimal 是精确的」要加限定:构造精确,运算受 context。3) 全局与局部上下文?——getcontext 按线程独立,全局改影响同线程所有后续运算;with localcontext() as ctx: ctx.prec = 50 局部生效,出 with 恢复——这是唯一推荐的临时改法。4) 生产陷阱?——模块 import 期改全局 prec 污染他人;quantize 忘提 prec 抛 InvalidOperation;以为 Decimal 运算无舍入误差(只是可控、可预期)。

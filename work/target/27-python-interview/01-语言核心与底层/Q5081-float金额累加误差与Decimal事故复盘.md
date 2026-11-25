---
title: "[Q5081] float 金额累加误差与 Decimal 迁移事故复盘"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5081 · float 金额累加误差与 Decimal 迁移事故复盘

难度：★★★☆☆ ｜ 标签：数值精度 / 事故复盘 / 金额计算

**问**：对账系统里 100 万笔金额用 `float` 累加后与数据库 SUM 差了 0.01 元，为什么逐笔核对每一条都对不上差值？改用 `Decimal` 就一定安全吗？

**答**：
- **结论**：`float` 是二进制浮点（IEEE 754 double），0.1 这类十进制小数无法精确表示，累加时误差单向累积且**不在单笔上体现**——每笔的四舍五入误差被"摊平"在结果里，逐笔比对必然找不到差异行。这是典型的事故特征：总量对不上、明细全对。
- **取舍**：修复路径有三档——`math.fsum`（补偿求和，把已有 float 列表加对，但不改变"金额不该用 float"的本质）；`Decimal`（十进制精确，代价是慢 10-100 倍且必须 `str`/`int` 构造，不能从 float 构造后再救）；整数分（amount_cents），最快也最稳。
- **实战**：事故复盘时的关键动作不是换类型了事，而是定边界——`Decimal` 只解决表示精度，`Decimal(0.1)` 依然带进 float 的脏值（必须 `Decimal("0.1")`）；且 `Decimal` 与 float 混合运算直接 `TypeError`，ORM 驱动返回类型要一并核对。金额字段在协议层就该定为 `string`（JSON number 会被 JS double 吃掉精度）。

```python
"""金额累加误差事故复盘：float / fsum / Decimal / 整数分"""
from decimal import Decimal, ROUND_HALF_UP
import random, math

random.seed(42)
# 模拟 100 万笔 0.01~9999.99 的金额
n = 1_000_000
amounts = [random.randrange(1, 1_000_000) / 100 for _ in range(n)]

total_float = sum(amounts)                 # float 累加
total_fsum = math.fsum(amounts)            # 补偿求和（float 世界内的"正确"）
total_dec = sum((Decimal(str(a)) for a in amounts), Decimal("0"))
cents = sum(round(a * 100) for a in amounts) / 100  # 整数分

print(f"sum(float)   = {total_float:.6f}")
print(f"fsum(float)  = {total_fsum:.6f}")
print(f"Decimal      = {total_dec}")
print(f"整数分        = {cents:.2f}")
print(f"sum vs fsum  差值: {total_float - total_fsum:+.6f}")

# 经典展示：0.1 + 0.2 != 0.3
print(repr(0.1 + 0.2))            # 0.30000000000000004
print(Decimal(0.1))               # 从 float 构造：脏值带进来了！
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

# 舍入必须显式指定，Decimal 的 / 会产生 28 位精度
q = (Decimal("10.005") / 3).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("quantize:", q)
```

**追问链**
1. 为什么 `math.fsum` 能把 float 求和做"对"，它用了什么算法？
   1. Shewchuk 算法：维护一个部分和小数组，把每一项的低丢失位精确并入中间量，最终一次舍入——它是 float 语义下的精确和，但仍是"对脏值的精确求和"，救不了"金额不该是 float"的设计错误。
2. 为什么 JSON 协议层金额建议传 string 而不是 number？
   1. JSON number 在多数客户端（尤其 JS）按 double 解析，`2^53` 以上或两位小数都可能被客户端层破坏；服务端改成 Decimal 也拦不住前端丢精度，所以契约层用 string + 服务端 `Decimal` 校验。
   2. 追问：Go/Java 侧呢？——Java 有 BigDecimal、Go 有 shopspring/decimal，跨语言一致性靠"整数分 + string 传输"这条最低公约数最稳。

## 背诵要点
- float 误差在累加中摊平，逐笔对账找不到差异行；`0.1+0.2 != 0.3`。
- 修复三档：fsum（治标）/ Decimal(str 构造)（治本）/ 整数分（最快最稳）；`Decimal(0.1)` 是脏值。
- 契约层金额传 string，防 JS double 吃精度；Decimal 舍入要显式 quantize。

## 复盘追问
- 如果 DB 列是 NUMERIC 但驱动返回 float，问题出在哪一层、怎么在 CI 拦住？
- Decimal 慢 10-100 倍，热点路径的金额计算如何在不放弃精度的前提下提速？

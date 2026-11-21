---
title: [Q1544] round 的银行家舍入:half-even 与财务口径
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1544 · round 的银行家舍入:half-even 与财务口径

> 难度:★★★☆☆ | 标签:round, 舍入, 浮点数

**问**:round(2.5) 为什么是 2 不是 3?float 的 round(x, 2) 为什么可能出现 2.675 → 2.67?

**答**:round 采用 round-half-to-even(银行家舍入):恰好在 .5 时舍向偶数——round(0.5)=0、round(1.5)=2、round(2.5)=2;长期统计无方向性偏差,是 IEEE 754 的默认选择。2.675 → 2.67 不是 bug:float 存的 2.675 本来就略小(用 Decimal(2.675) 可见),按真实二进制值舍入自然落在 2.67。要点:① round(x) 返回 int,round(x, n) 返回同类型 float;ndigits 为负是舍到十位百位(round(1250, -2)=1200,同样 half-even);② f-string/format 展示走同一套 half-even;③ 财务「五入」口径用 Decimal.quantize + ROUND_HALF_UP 显式指定,把舍入策略留在调用点可见;④ round 不是精度修复工具,只在展示与对齐层有意义。

```python
# file: code/01_语言核心与底层/q1544_bankers_rounding.py
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

CASES = [0.5, 1.5, 2.5, 3.5, -0.5, -2.5]


def show_half_even():
    return [round(x) for x in CASES]


if __name__ == "__main__":
    print("round cases:", list(zip(CASES, show_half_even())))

    print("2.675 ->", round(2.675, 2), "| stored as:", Decimal(2.675))
    print("format same:", f"{2.675:.2f}")

    # ndigits 为负:舍到十位百位
    print("round(1234, -2):", round(1234, -2),
          "| round(1250, -2):", round(1250, -2), " 半到偶")

    # 财务口径:Decimal 显式 HALF_UP
    money = Decimal("2.675")
    print("decimal half_up  :", money.quantize(Decimal("0.01"), ROUND_HALF_UP))
    print("decimal half_even:", money.quantize(Decimal("0.01"), ROUND_HALF_EVEN))

    # Decimal 的 round 也走 half-even(上下文舍入)
    print("round(Decimal):", round(Decimal("2.5")), round(Decimal("3.5")))
```

**追问**:1) Python 3 为什么不给 round 提供 half-up?——half-even 是 IEEE 754 默认且统计无偏;要 half-up 显式走 Decimal.quantize 指定 ROUND_HALF_UP,把「舍入口径」留在调用点可见。2) 银行家舍入的实际表现?——round(2.5)=2、round(3.5)=4(取偶);另注意 2.675 实际是 2.67499...(二进制表示),round 后得 2.67——表示误差先于舍入规则起作用。3) 正解路径?——财务金额全程 Decimal,quantize(Decimal("0.01"), ROUND_HALF_UP);格式化 f"{:.2f}" 同样是 half-even,不要当业务舍入用。4) 生产陷阱?——用 round 做金额舍入(口径错误+表示误差);测试期望 half-up 而拿到 half-even;Python 2 的 round 是 half-away,跨版本行为差异。

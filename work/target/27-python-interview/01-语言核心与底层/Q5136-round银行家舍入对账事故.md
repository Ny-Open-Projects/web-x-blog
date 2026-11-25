---
title: [Q5136] round 银行家舍入的对账事故复盘
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5136 · round 银行家舍入的对账事故复盘

难度：P6 | 标签：round、银行家舍入、浮点表示、事故复盘

**问**：财务同学反馈 `round(2.675, 2)` 结果是 2.67 而不是 2.68，另一个系统 `round(0.5)` 返回 0 而不是 1，两笔对账差了分钱。请解释 Python round 的真实语义、与"四舍五入"直觉的差异来源，以及金额处理的正确方案。

**答**：

**结论**：Python 3 的 `round` 用"银行家舍入"（round-half-to-even）：恰好 .5 时向最近的偶数取整，所以 `round(0.5)=0`、`round(1.5)=2`、`round(2.5)=2`。这消除了长期累加 half-up 舍入的系统性上偏，是统计上更公平的策略。而 `round(2.675, 2)=2.67` 的元凶不是舍入策略而是二进制浮点：2.675 的真实存储值是 2.67499999999999982...，比 2.675 略小，舍入自然到 2.67。两个问题叠加造成"按十进制思维写的对账逻辑"与实际差一分。

**取舍**：金额的正确方案是全程 `decimal.Decimal`（十进制精确表示）+ `ROUND_HALF_UP`/`ROUND_HALF_EVEN` 显式指定量化策略， monetary 值绝不经 float 中转；接口层用字符串或整数最小单位（分）传输。若历史代码困在 float，用 `round(x, 2) + 校验` 不可靠，正确补救是 `Decimal(str(x))`——注意必须 `str()` 中转让 Decimal 拿到"十进制字面值"而不是 float 的二进制真值。

**实战**：事故复盘套路：先把两侧行为在各自精度下复现（写死输入输出），确认差异是"舍入模式"还是"表示误差"；再统一舍入契约（半上/半偶必须全链路一致，跨语言 Java half-up 与 Python half-even 不同是跨国对账常见坑）。

```python
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# 1) 银行家舍入：.5 向偶数取整
print("round(0.5)  =", round(0.5))     # 0
print("round(1.5)  =", round(1.5))     # 2
print("round(2.5)  =", round(2.5))     # 2

# 2) 二进制表示误差：2.675 存的不是 2.675
print("repr(2.675) =", repr(2.675))
print("round(2.675, 2) =", round(2.675, 2))     # 2.67

# 3) float 直接转 Decimal 会继承误差，str 中转才拿字面值
print("Decimal(2.675)    =", Decimal(2.675))
print("Decimal(str(2.675))=", Decimal(str(2.675)))

# 4) 金额正确姿势：Decimal + 显式舍入模式
def money_round(x: str, places="0.01") -> Decimal:
    return Decimal(x).quantize(Decimal(places), rounding=ROUND_HALF_UP)

print("money('2.675') ->", money_round("2.675"))          # 2.68
print("money('2.685') ->", money_round("2.685"))          # 2.69（half-up）
print("half-even('2.675') ->",
      Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN))
```

**追问 1**：为什么 `round(x, n)` 对负数位数（如 round(1234, -2)）也是 half-even？
答：round 的 half-even 规则与位数无关，作用于十进制意义的目标位；`round(1250, -2)=1200`、`round(1350, -2)=1400`，向偶数百位取整，这与很多语言 round half-away-from-zero 的结果不同。

**追问 2**：Decimal 运算有没有精度问题？
答：有界但存在：默认上下文 28 位有效数字，乘除可能触发舍入，需用 `getcontext().prec` 或 localcontext 控制；且 Decimal 与 float 混算直接抛 TypeError，强制你划清边界——这反而是优点。

**追问 3**：numpy 的 round 与内置 round 语义一致吗？
答：`numpy.round` 同为 half-to-even；C/Java 的 `printf("%.2f")` 多为 half-even（IEEE 754 默认），而 Java `BigDecimal`/`DecimalFormat` 默认 HALF_UP——跨语言对账必须显式统一模式。

## 背诵要点

- Python 3 round 是 round-half-to-even：round(0.5)=0、round(2.5)=2，为消除系统性上偏。
- round(2.675,2)=2.67 是 float 二进制表示误差（2.6749999...），不是舍入策略问题。
- 金额全程 Decimal（str 中转）+ 显式 quantize 舍入模式；跨语言对账先统一 half-up/half-even。

## 复盘追问

- 若外部接口只给你 float 金额，如何在边界层止血？(提示：Decimal(str(x)) + 定点整数化)
- 如何在 CI 里防止新代码把金额再次经过 float？(提示：自定义 lint 禁止 float 参与金额字段运算)

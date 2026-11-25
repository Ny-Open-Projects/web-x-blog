---
title: "[Q5266] float.as_integer_ratio：二进制小数的精确分数与往返边界"
date: 2026-11-25
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5266 · float.as_integer_ratio：二进制小数的精确分数与往返边界

难度：P6 ｜ 标签：float、as_integer_ratio、Fraction、浮点、精度、Decimal

基线：CPython 3.12.2，纯标准库；用 `float.as_integer_ratio`、`fractions.Fraction` 与 `math` 验证精确分数、往返与特殊值。

**问**：风控规则引擎要判断"金额比例是否超过 0.1"，配置里写 `threshold=0.1`，代码用 `ratio > threshold`。测试环境 10.0000001% 能过、9.9999999% 也不过，线上却出现边界单子两边都判错；另一个团队把 `0.1` 序列化成 `"1/10"` 存进数据库，回读用 `Fraction(1, 10)`，和原来的 float 比较全都不相等。`0.1` 在 float 里到底是什么？`as_integer_ratio()` 给出的分数能不能无损还原？为什么不能用它来"把 0.1 变成 1/10"？

**答**：

- **结论**：`float` 是二进制浮点，`0.1` 无法精确表示，实际值是 `3602879701896397 / 36028797018963968`（分母是 `2^55`），比数学上的 1/10 略大。`x.as_integer_ratio()` 返回**精确等于该 float** 的 `(numerator, denominator)`，分母一定是 2 的幂（正规数、次正规数都成立），并且 `float(n/d)` 能无损还原原来的 float。它不是"人类可读的分数化简"：`(0.1).as_integer_ratio()` 不会给你 `(1, 10)`，因为那会改变值。`0.0` 返回 `(0, 1)`，`-0.0` 也返回 `(0, 1)`（符号信息丢失，需要 `math.copysign` 判断）；`inf` 抛 `OverflowError`，`nan` 抛 `ValueError`。
- **取舍**：要"精确的十进制语义"（金额、税率、比例阈值）应该用 `Decimal("0.1")` 或整数分，而不是 float + 分数；要"精确保留一个已有 float 的值"（序列化、跨语言传输、黄金测试基线）才用 `as_integer_ratio`，它保证 round-trip。`Fraction.from_float(x)` 与 `as_integer_ratio` 等价，但 `Fraction(1, 10)` 是精确的 1/10，和 `Fraction.from_float(0.1)` 不相等——这是两套语义，不能混用。另一个取舍是可读性：`(3602879701896397, 36028797018963968)` 很长，传输时可以用 `float.hex()`（也是精确的）或 `struct.pack`，但 hex 对人类更不友好。
- **实战**：规则引擎的事故是把"配置解析"和"运行时比较"用了两套表示：配置侧 `Decimal(str(0.1))` 得到 0.1，运行侧 `float` 得到略大于 0.1 的值，边界自然不一致。修复：① 比例统一用 `Decimal`，配置从字符串 `"0.1"` 解析，禁止从 float 转；② 如果必须用 float，比较时加 `math.isclose(ratio, threshold, rel_tol=1e-12)` 或把阈值转成整数基点（1000 表示 10%）；③ 序列化用 `as_integer_ratio` 只用于"保存原始 float 做回归测试"，不用于业务语义。上线后边界投诉归零。

下面验证 `0.1` 的真实分数、分母为 2 的幂、`float(n/d)` 往返、`Fraction` 两种构造的差异、特殊值与 `-0.0` 的符号。

```python
# float.as_integer_ratio: 精确等于该 float 的分数, 分母必为 2 的幂
import math
from fractions import Fraction

x = 0.1
n, d = x.as_integer_ratio()
print("[1] 0.1 的精确分数:", n, "/", d)
assert (n, d) == (3602879701896397, 36028797018963968)
assert d & (d - 1) == 0, "分母必须是 2 的幂"
assert float(n / d) == x, "n/d 必须无损还原"

# 与 Fraction 的两种构造对比
exact = Fraction.from_float(x)
decimal_idea = Fraction(1, 10)
print("[2] Fraction.from_float == 1/10 ?", exact == decimal_idea)
print("    exact - 1/10 =", exact - decimal_idea)
assert exact == Fraction(n, d)
assert exact != decimal_idea
assert exact > decimal_idea, "0.1 的 float 值略大于 1/10"

# 常见值的规范形式
for value, expected in [(0.5, (1, 2)), (1.0, (1, 1)), (0.0, (0, 1)), (2.0, (2, 1))]:
    got = value.as_integer_ratio()
    print(f"[3] {value!r}.as_integer_ratio() = {got}")
    assert got == expected

# 负零: 比值丢符号, 要用 copysign 判断
neg_zero = -0.0
print("[4] -0.0 ratio:", neg_zero.as_integer_ratio(), "signbit:", math.copysign(1.0, neg_zero))
assert neg_zero.as_integer_ratio() == (0, 1)
assert math.copysign(1.0, neg_zero) == -1.0

# 次正规数同样满足"分母 2 的幂 + 可往返"
tiny = 5e-324
tn, td = tiny.as_integer_ratio()
print("[5] 最小次正规数: numerator bits =", tn.bit_length(), "denominator bits =", td.bit_length())
assert td & (td - 1) == 0
assert float(tn / td) == tiny

# 特殊值
for special, error in [(float("inf"), OverflowError), (float("-inf"), OverflowError), (float("nan"), ValueError)]:
    try:
        special.as_integer_ratio()
        raise AssertionError(f"{special!r} 本应报错")
    except error as exc:
        print(f"[6] {special!r} -> {type(exc).__name__}")

print("[7] 结论: 精确分数用于保留 float, 业务十进制语义请用 Decimal 或整数分")
```

**追问一**：既然 `float(n/d)` 能还原，为什么不能把所有 float 都序列化成 `n/d` 再回读？—— 可以，但要处理三个边界：① 分母可能极大（次正规数的分母有几百位），文本体积膨胀；② 解析方必须支持任意精度整数，JSON 的 number 会退化成 float，必须用字符串；③ `-0.0`、`inf`、`nan` 不在有理数范围内，要额外的哨兵编码。更常见的精确序列化是 `float.hex()`（如 `0x1.999999999999ap-4`），它同样是往返精确的，且长度固定；`as_integer_ratio` 更适合在进程内做精确算术，而不是跨语言协议。

**追问二**：`Decimal(0.1)` 和 `Decimal("0.1")` 为什么不同？—— `Decimal(0.1)` 接收的是已经变成二进制浮点的值，会把这个**近似值**完整展开成十进制（`0.1000000000000000055511151231257827...`）；`Decimal("0.1")` 从字符串解析，得到精确的 0.1。这是"输入是 float 还是 str"的区别，不是 Decimal 的 bug。金融系统里必须从字符串或整数分构造 Decimal，任何经过 float 的路径都已经丢失了十进制语义。

## 背诵要点

- `as_integer_ratio()` 返回精确等于该 float 的 `(n, d)`，分母必为 2 的幂，`float(n/d)` 无损往返。
- `0.1` 的真实值是 `3602879701896397/36028797018963968`，略大于 1/10；`Fraction.from_float(0.1) != Fraction(1, 10)`。
- `-0.0` 的 ratio 是 `(0,1)`，符号要用 `math.copysign`；`inf` 抛 `OverflowError`，`nan` 抛 `ValueError`。

## 复盘追问

- 为什么分母一定是 2 的幂？（float 的尾数是二进制小数，值 = mantissa × 2^exp，通分后分母只含因子 2）
- 什么时候该用 `float.hex()` 而不是 `as_integer_ratio()`？（需要定长、可读、跨语言精确传输时用 hex；需要进程内精确有理运算时用 ratio）

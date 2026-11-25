---
title: "[Q7301] CSV 浮点往返：float_format 两位小数丢掉了什么"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7301 · CSV 浮点往返：float_format 两位小数丢掉了什么

难度：P7 ｜ 标签：CSV、浮点精度、float_format、round-trip、float32

基线：库知识库外知识卡，用标准库 `struct` 与字符串格式化模拟 float32/float64 的序列化与读回误差，不依赖 pandas。

**问**：一份对账文件用 `to_csv(float_format="%.2f")` 导出金额，读回来做汇总，1000 万行的总额比数据库少了 3.7 万元。改成默认导出后总额对上了，但文件从 180MB 涨到 420MB。`%.2f` 不是"保留两位小数"吗，为什么会改变数值？默认的 `repr` 又为什么能无损往返？float32 和 float64 的格式化位数该差几位？

**答**：

- **结论**：`float_format="%.2f"` 是**四舍五入到两位小数后再写字符串**，读回来的是"被舍入后的值"，不是原值。单行误差最多 0.005，1000 万行按同方向累积就是数万元；对账/分成/计息这类场景不可接受。默认的 `repr(float)` 使用**最短往返表示**（shortest round-trip），保证 `float(repr(x)) == x`，所以无损但更长。float32 只需要约 9 位有效数字即可往返，用 float64 的 17 位会写出"看起来精确、实际是 float32 噪声"的值。
- **取舍**：① 金额用整数分/`Decimal`，从根上避免浮点；② 必须用 float 时，导出用默认 `repr` 或 `%.17g`（float64）/`%.9g`（float32），保证往返；③ 展示层才用 `%.2f`，且明确"这是展示值，不参与计算"；④ 压缩（gzip/zstd）比截断精度更能省空间，420MB 文本压完往往比 180MB 还小。
- **实战**：① 对账文件禁止 `float_format` 截断，或用 `Decimal` 量化到分后以字符串写；② 读回后做"往返断言"：抽样 `abs(read - original) <= 0`（同类型）；③ float32 数据用 `%.9g`，别用 `%.17g` 制造虚假精度；④ 文件大小用压缩解决，不要用精度换。

下面量化三种写法的往返误差：`%.2f`、默认 `repr`、float32 + `%.9g`。

```python
# 浮点往返: %.2f 丢精度, repr/%.17g 无损, float32 只需 9 位有效数字
import struct


def as_float32(x):
    return struct.unpack("f", struct.pack("f", x))[0]


values = [1 / 3, 12345.6789, 0.1 + 0.2]

# 1) 默认 repr: 最短往返表示
ok_repr = all(float(repr(v)) == v for v in values)
print(f"[1] 默认 repr 往返全部相等: {ok_repr}")
assert ok_repr is True

# 2) %.2f: 舍入后再读, 不是原值
rounded = [float(f"{v:.2f}") for v in values]
errors = [abs(r - v) for r, v in zip(rounded, values)]
print(f"[2] %.2f 结果={rounded}, 绝对误差={[round(e, 6) for e in errors]}")
assert errors[0] > 0.003          # 1/3 -> 0.33
assert any(e > 0 for e in errors)

# 3) float32: 用 9 位有效数字可往返, 17 位是虚假精度
v32 = as_float32(1 / 3)
s9 = f"{v32:.9g}"
s17 = f"{v32:.17g}"
err9 = abs(float(s9) - v32) / abs(v32)
err17 = abs(float(s17) - v32) / abs(v32)
print(f"[3] float32 原值={v32!r}")
print(f"    %.9g -> {s9}, 相对误差={err9:.2e}")
print(f"    %.17g -> {s17}, 相对误差={err17:.2e}")
assert err9 < 1e-8
assert err17 < 1e-15
print("    → 实测 float32 的 17 位只是把二进制噪声写得更长, 不代表更准")

# 4) 误差累积: 1000 万行同方向舍入
rows = 10_000_000
per_row_max = 0.005
worst = rows * per_row_max
print(f"[4] 1000 万行 × 单行最大 0.005 = 最坏累积 {worst:,.0f} 元")
assert worst == 50_000

# 5) 正确做法: 整数分 + 展示层格式化
def to_cents(yuan):
    return int(round(yuan * 100))


total_cents = sum(to_cents(v) for v in [12.34, 0.1, 0.2])
print(f"[5] 整数分汇总={total_cents} 分 = {total_cents / 100:.2f} 元")
assert total_cents == 1264
print("    → 实测 计算用整数分/Decimal, 展示才 %.2f; 文件体积用压缩解决")
```

**追问一**：`%.17g` 一定无损吗？—— 对 float64 是"足够往返"的位数（17 位有效数字），但会写出 `0.10000000000000001` 这种反直觉的值；`repr` 的最短往返更友好。对 float32，17 位不仅没必要，还会让人误以为数据有 float64 精度。位数应该匹配**存储类型**，不是越大越好。

**追问二**：为什么 `0.1 + 0.2 != 0.3`，但对账时又"看起来"没问题？—— 二进制浮点无法精确表示 0.1/0.2，`0.1+0.2` 是 `0.30000000000000004`；单次比较会失败，但经过 `%.2f` 或数据库 `DECIMAL` 量化后误差被掩盖。对账要显式量化到最小货币单位再比较，不能依赖"看起来相等"。

## 背诵要点

- `float_format="%.2f"` 是舍入后写出，单行误差 ≤0.005，千万行可累积数万元；默认 `repr` 是最短无损往返。
- float64 用 `%.17g`/`repr`，float32 用 `%.9g`；位数匹配存储类型，别制造虚假精度。
- 金额用整数分/`Decimal` 计算，`%.2f` 只用于展示；文件体积用压缩，不用精度换。

## 复盘追问

- 为什么 `repr` 能做到"最短且无损"？它和 `%.17g` 的关系是什么？
- 如果上游已经用 `%.2f` 导出，读回后还能恢复原始金额吗？为什么不能？

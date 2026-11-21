---
title: [Q5026] isdigit 三兄弟：字符串校验与 int() 的对齐问题
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5026 · isdigit 三兄弟：字符串校验与 int() 的对齐问题

> 难度:★★★☆ | 标签:isdigit, Unicode, 校验

**问**：`str.isdigit()`、`str.isdecimal()`、`str.isnumeric()` 三个方法长得很像，判定范围差在哪？用 `isdigit()` 做"能转成整数"的前置校验为什么会翻车——`"²".isdigit()` 是 True 但 `int("²")` 抛异常，反过来 `int("１２３")` 全角也能转。校验和解析怎么对齐？

**答**：三个方法对应 Unicode 的三个属性类，范围递增：**isdecimal ⊂ isdigit ⊂ isnumeric**。`isdecimal()` 只认 `Nd`（Decimal_Number，含全角数字、阿拉伯-印度数字等十进制系）；`isdigit()` 额外包含 `No` 里的 digit 字符（如上标 `²`）；`isnumeric()` 再纳入 `Nl`（罗马数字 Ⅳ）与 `No` 的分数（½）、CJK 数字（零）。而 `int()` 的解析面与 **isdecimal 精确对齐**：`int()` 接受所有 Nd 数字（所以 `int("١٢٣")` 出 123、`int("１２３")` 出 123——国际化输入合法），但拒绝 `²/½/Ⅳ`。事故模式：校验用 `isdigit()`（"²"通过）、解析用 `int()`（炸 ValueError）；或反着——校验只认 ASCII 正则、却把全角数字拒之门外（而 `int()` 本来支持）。纪律：**"能转整数吗"的判定就是 `s.isdecimal()`**，与 `int()` 完全同面；`isdigit/isnumeric` 是语义判定（"这是个数字字符"），不是解析判定。浮点解析同理对齐 `float()` 的接受面（`inf/nan` 字符串也能被 `float()` 解析，Q534/Q686）。负号/正号不属于任何数字类，`"-1"` 三个方法全是 False——校验要显式处理符号。

```python
# file: code/01_语言核心与底层/q5026_digit_checks.py
cases = ["12", "12.5", "-1", "²", "½", "١٢٣", "１２３", "零", "Ⅳ"]
for c in cases:
    try:
        parsed = f"int={int(c)}"
    except ValueError:
        parsed = "int 失败"
    print(f"{c!r:<8} isdigit={str(c.isdigit()):<5} isdecimal={str(c.isdecimal()):<5} "
          f"isnumeric={str(c.isnumeric()):<5} {parsed}")

print()
print("对齐结论: int() 的接受面 == isdecimal()(Nd 类全集,含全角/阿拉伯-印度数字)")
print("事故一: isdigit 放行 '²' -> int() 炸 ValueError(校验与解析不同面)")
print("事故二: 正则只认 [0-9] -> 拒掉 int() 本可解析的全角/阿拉伯输入")
print("纪律: 要解析就 isdecimal() 前置 + int() try/except 兜底,别用 isdigit/isnumeric 当解析门卫")
```

**追问**：1) 为什么 `int("１２３")` 能转而 `int("½")` 不能？——`int()` 按 Unicode 的 decimal digit value 逐字符换算（`unicodedata.digit(c)`），全角/阿拉伯数字有明确的十进制位值；`½` 只有数值（`numeric()`）没有位值，无法按位拼数。2) `float("nan")`、`float("inf")` 为什么能解析，校验该怎么防？——`float()` 额外接受 `nan/inf/infinity` 及大小写变体（C 标准遗产），JSON 层不会出现（JSON 规范不含 NaN，Q686），但直接 `float(用户输入)` 的表单/参数解析会放行——数值校验用 `isdecimal()`（配合小数点判断）或显式白名单，不要裸 `float()`。3) `unicodedata.digit/numeric/decimal` 三个函数和三个方法什么关系？——单字符级对应：`decimal(c)` 有值 ⇔ `c.isdecimal()`；`digit(c)` 覆盖上标等 ⇔ isdigit 面；`numeric(c)` 最大 ⇔ isnumeric 面。

## 背诵要点
1. 范围递增：isdecimal（Nd）⊂ isdigit（+digit 字符如 ²）⊂ isnumeric（+Nl/分数/CJK 数字）。
2. `int()` 的解析面 == isdecimal：全角/阿拉伯-印度数字能转（123），上标/分数/罗马数字不能。
3. 校验与解析必须同面："能转整数"用 isdecimal() + try/except；"-1" 不属于任何数字类要显式处理符号。

## 复盘追问
1. 一个国际化表单出现了"阿拉伯数字也能下单"的投诉，是校验漏了还是解析错了？（提示：两层都对——int() 本就接受 Nd；要限制 ASCII 用正则 [0-9] 白名单，先想清楚产品语义再定校验面）
2. `int("１２３")` 入库后与 `"123"` 相等吗？排序/去重会有什么坑？（提示：值相等（都是 int 123）但若整串以 str 入库则 "１２３" != "123"——入口归一化（NFKC 或先转 int）是唯一可靠解）

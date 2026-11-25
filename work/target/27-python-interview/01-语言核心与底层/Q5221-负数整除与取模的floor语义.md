---
title: "[Q5221] 负数整除与取模的 floor 语义：// 与 % 的符号跟随"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5221 · 负数整除与取模的 floor 语义：// 与 % 的符号跟随

难度：P6 ｜ 标签：整除、取模、divmod、floor 除法、跨语言移植、负数边界

**问**：`-7 // 2` 和 `-7 % 2` 在 Python 里各是多少？为什么说"Python 的整除是 floor 除"会伤到从 C/Java 移植的代码？`divmod` 的不变量是什么？想要 C 语义该怎么写？负数分页/分片场景有哪些踩坑？

**答**：
结论：Python 的 `//` 是 **floor 除**（向负无穷取整），`%` 的结果符号**跟随除数**——`-7 // 2 == -4`、`-7 % 2 == 1`。C/Java/Go 是**截断除**（向零取整），对应 `-3` 和 `-1`。这组差异不是 bug，而是语言约定：floor 语义保证了不变量 `a == b * (a // b) + a % b` 对**任意符号组合**成立，且取模结果落在 `[0, b)`（b 为正）——这对环形缓冲、哈希桶、周期调度是天然友好的；截断语义则在负数时让 `%` 可能返回负值，用它当数组下标直接越界。移植事故的高发面：分页 `offset // size`（offset 可能为负）、分桶 `hash % n`（负哈希）、时间对齐 `ts // period`（epoch 前的时间戳）、游戏/图形里 C 教材写法的照搬。想要 C 语义用 `math.trunc(a / b)` 或 `int(a / b)`（注意大整数时浮点精度问题，应改用 `math.fmod` 或符号分支），想要 floor 直接 `//`；`math.fmod(a, b)` 给的是 C 语义余数（符号跟随被除数）。

取舍：a) 业务上"取整"几乎都该想清楚方向：`//`（floor）、`trunc`（向零）、`round`（half-even，见 Q5136）三者语义不同，评审时看到对可能为负的数做 `//`/`%` 就要问一句方向对不对；b) 环形/周期场景坚持 floor 语义（Python 默认），负数自动回绕，最省心；c) 与外部系统对齐时（协议、SQL、前端 JS），显式写 `trunc` 分支并加注释，不要依赖对方"恰好都传正数"；d) `divmod` 一次调用同时拿商和余，且语义与 `//`+`%` 一致，优先用；e) 对极端大整数不要走 `int(a / b)`——浮点只有 53 位精度，会算错，用 `math.trunc` 也不够，需 `a // b` 配符号修正或 `-(-a // b)` 这类整数技巧。

实战：事故形态是"分页组件从 Java 版移植，`offset` 意外传入 -1，Java 里 `-1 / 20 == 0`，Python 里 `-1 // 20 == -1`，SQL 拼出 `LIMIT 20 OFFSET -1` 直接报错；修复为入口钳位 `max(offset, 0)` 并补 floor 语义说明"。下面演示四种符号组合、不变量校验与 C 语义替代写法。

```python
# 负数整除与取模: floor 语义 (// 与 % 符号跟随除数)
pairs = [(-7, 2), (7, -2), (-7, -2), (7, 2)]
print("[1] Python 的 floor 除: a//b 向负无穷取整, a%b 符号跟随 b")
for a, b in pairs:
    q, r = divmod(a, b)
    print(f"    {a} // {b} = {q:>3}, {a} % {b} = {r:>3}, divmod = {q, r}")

print("[2] 不变量: a == b * (a//b) + a%b 对任意符号成立")
for a, b in pairs:
    q, r = divmod(a, b)
    assert a == b * q + r, (a, b, q, r)
print("    全部符号组合校验通过")

print("[3] C/Java 风格是截断除, Python 是 floor 除 -> 移植必踩")
c_style = [int(a / b) for a, b in pairs]          # int() 截断小数, 向零取整
for (a, b), cq in zip(pairs, c_style):
    print(f"    {a}/{b}: Python floor={a//b}, 截断={cq}, 差异={a//b - cq}")

print("[4] 想要 C 语义时用 math.trunc / int(除法), 想要 floor 用 //")
import math
print("    math.trunc(-7/2) =", math.trunc(-7 / 2), " | -7//2 =", -7 // 2)
print("    math.fmod(-7, 2) =", math.fmod(-7, 2), " (C 语义余数, 符号跟随被除数)")
print("[5] 分页负值防护: n//size 对 n=-1 得 -1, 应先钳到 0")
n, size = -1, 20
print("    max(n, 0)//size =", max(n, 0) // size)
```

**追问一**：为什么 floor 语义让 `%` 能安全当环形索引用？—— 因为 `b > 0` 时 floor 语义保证 `a % b` 恒在 `[0, b)`，与 `a` 的符号无关：`-1 % 24 == 23`，"昨天的 23 点"自动回绕；而截断语义下 `-1 % 24 == -1`，直接越界。同理时间窗对齐（`ts // period * period`）用 floor 才能对负值（epoch 前）也得到"包含该时刻的窗口起点"。这是 Python 选 floor 除的实际收益：数值语义与"桶"的物理直觉一致。

**追问二**：`-(-a // b)` 这类整数技巧在干什么？什么时候用？—— 这是**向上取整**（ceiling）的整数写法：`-(-a // b)` 等价于 `ceil(a / b)` 且全程无浮点，大整数安全。用在"至少要几个桶/几批"的场景（容量计算、分片数）。注意三种取整 `a//b`（floor）、`-(-a//b)`（ceil）、`round(a/b)`（half-even）方向不同；对可能为负的 `a`，ceiling 公式会失效，要么先钳位要么显式分支。整数技巧的代价是可读性，写清楚注释比技巧本身更重要。

## 背诵要点
- Python `//` 是 floor 除（向负无穷），`%` 符号跟随除数且 b>0 时恒在 [0,b)；C/Java 是截断除，移植负数必错。
- 不变量 `a == b*(a//b) + a%b` 全符号成立；C 语义用 `math.trunc`/`math.fmod`，ceil 用 `-(-a//b)`（a 非负时）。
- 高危面：分页 offset、负哈希分桶、epoch 前时间戳对齐；入口钳位 + 显式写明取整方向。

## 复盘追问
- 从 Java 移植的分页组件在负 offset 上行为不同，根因？（floor vs 截断除；入口钳位 max(offset,0)）
- 为什么 Python 选 floor 语义而不是截断？（% 恒非负，环形索引/周期对齐天然安全，不变量全符号成立）

---
title: "[Q5232] 复数与 cmath：不可比较序与复平面运算"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5232 · 复数与 cmath：不可比较序与复平面运算

难度：P5 ｜ 标签：complex、cmath、conjugate、polar/phase/rect、负数开方、比较 TypeError、复平面

**问**：Python 原生复数 `complex` 支持哪些运算、不支持哪些？为什么 `cmath.sqrt(-1)` 能算而 `math.sqrt(-1)` 崩？`abs(z)` 对复数返回什么？`cmath.polar/phase/rect` 三件套解决什么问题？复数在 JSON/数据库序列化时的常见做法是什么？

**答**：
结论：`complex` 是内建数值类型，`(a+bj)` 字面量直接构造，`real/imag` 是浮点分量、`conjugate()` 共轭；支持 `+ - * / **`、`abs()`（返回**模**，勾股长度，是浮点）、`==`（按分量相等），**不支持 `< <= > >=`**——复数没有全序，比较直接 TypeError，也因此 `sorted([z1, z2])`、`min/max` 都不能用。`math.sqrt(-1)` 报 ValueError：math 模块在实数域计算；`cmath.sqrt(-1)` 返回 `1j`：cmath 模块在**复平面**计算——判定标准是"运算的域"，不是"数值的类型"，`math.sqrt(4+0j)` 也会 TypeError（参数不接受复数）。`cmath.polar(z)` 给 `(模, 相位角)`、`phase(z)` 给辐角、`rect(r, phi)` 把极坐标转回复数——信号处理、旋转矩阵、阻抗计算的核心三件套。两条实战坑：①复数运算全程是浮点，`abs(complex(3,4))` 得 `5.0`，误差语义遵循浮点（Q537）；②复数不是 JSON/SQL 原生类型，序列化要拆成 `[real, imag]` 对或字符串化，反序列化侧 `complex(str)` 的解析规则与构造器不同（接受 `"1+2j"` 字面量形式）。

取舍：a) 需要平方根落在复平面的场景（信号、控制论）：选 `cmath`，一次 import 解决；b) 只做幅值/距离：`abs(z)` 是 C 级实现的勾股，比手写 `(re**2 + im**2) ** 0.5` 更防溢出（hypot 算法）；c) 排序需求：复数天生无序，业务要排序就得定义投影（按模或按相位），把"无序"显式化而不是 hack 比较；d) 性能敏感的实数域计算：坚持 `math`/`array('d')`，复数对象开销大（两个 double + 对象头）；e) 与 numpy 边界：纯 Python 复数适合零散运算，向量化数值计算应升级 numpy——标准库复数是"正确性工具"不是"吞吐工具"。

实战：事故形态是"DSP 配置校验里用 `min(allowed_gain)` 校验增益向量，向量是复数幅值表示，直接 TypeError；根因是上游把 `abs(z)` 的结果与原始复数混在同一个列表——修复为数据结构层面区分'复数域'与'幅值域'，排序/比较前显式投影 `abs()`"。下面实测复数运算边界与 cmath 三件套。

```python
# 复数与 cmath
import cmath
import math

z = complex(3, 4)
print("[1] 分量与共轭: real/imag/conjugate")
print("    z =", z, "| real =", z.real, "| imag =", z.imag, "| conjugate =", z.conjugate())

print("[2] abs() 是模 (浮点), 复数支持等值比较但不支持序比较")
print("    abs(3+4j) =", abs(z), "(类型:", type(abs(z)).__name__ + ")")
try:
    1 + 2j < 2 + 3j
except TypeError as e:
    print("    1+2j < 2+3j -> TypeError:", e)
print("    (1+2j) == (1+2j) ->", (1 + 2j) == (1 + 2j))

print("[3] math.sqrt(-1) 报错, cmath.sqrt(-1) 返回复平面解")
try:
    math.sqrt(-1)
except ValueError as e:
    print("    math.sqrt(-1) -> ValueError:", e)
print("    cmath.sqrt(-1) =", cmath.sqrt(-1))
try:
    math.sqrt(4 + 0j)
except TypeError as e:
    print("    math.sqrt(4+0j) -> TypeError: math 不接受复数参数 (域不同)")

print("[4] polar/phase/rect: 极坐标三件套")
w = cmath.rect(5, math.pi / 6)                       # 半径 5, 角 30 度
print("    rect(5, pi/6) =", w)
print("    polar(w) =", cmath.polar(w), "| phase(w) =", cmath.phase(w))
print("    cmath.exp(1j*pi) =", cmath.exp(1j * math.pi), "(欧拉公式)")

print("[5] 序列化边界: JSON 无复数类型, 常见做法是 [real, imag] 对")
import json
payload = {"z": [z.real, z.imag]}
back = complex(*json.loads(json.dumps(payload))["z"])
print("    round-trip:", json.dumps(payload), "->", back)
print("[6] 工程纪律: 复数域与幅值域在数据结构上分开; 排序前显式投影 abs/phase")
```

**追问一**：`cmath.sqrt` 返回的是哪个平方根？为什么需要主值分支（principal branch）？—— 复数的平方根有**两个**解（z 的两个平方根互为相反数），实数域约定"取非负的那个"，复数域没有正负序可依，于是约定**主值**：辐角落在 `(-pi, pi]` 半开区间的那支，`cmath.sqrt` 恒返回主值分支（实部非负；实部为零时虚部非负）。工程意义：多值函数（sqrt/log/atan）在复平面都要声明分支，`cmath.log(z, base)`、`cmath.log10` 同样按主分支——做频谱/相位展开时如果需要"另一个分支"，要自己加 `±` 对称分支，而不是指望库替你选。这也是数值库 API 设计的通用范式：多值运算显式声明分支，调用方显式选择。

**追问二**：为什么复数没有全序？数学上"不能比大小"对 API 设计的启发是什么？—— 复数与序的冲突点：任何全序要保持与代数运算的兼容（如 a<b 则 a+c<b+c）都会与复数代数性质矛盾——i²=-1 会推出 i>0 与 -i>0 同时成立的悖论，所以数学上复数域不是有序域。Python 的选择是**序运算直接 TypeError**而不是定义一个武断的字典序——"不定义"比"乱定义"更安全：字典序会让 `sorted` 静默给出违反直觉的结果，TypeError 让错误在使用点暴露。启发：给"数学上无序/无意义的操作"设计 API 时，宁可让它显式失败，也不要给一个看似可用的错误语义（同类先例：NaN 的任何比较都返回 False，Q534）。业务侧要排序复数集合，就显式定义投影键（按模/按相位/按实部），让业务语义出现在代码里。

## 背诵要点
- complex 支持 +-*/ **、abs()=模、==；不支持 < <= > >=（复数无全序，比较 TypeError）。
- math 在实数域（负数开方 ValueError），cmath 在复平面（sqrt(-1)=1j）；polar/phase/rect 是极坐标三件套，多值函数取主值分支。
- JSON/SQL 无复数类型：序列化拆 [real, imag] 或 complex(str)；排序前显式投影。

## 复盘追问
- math.sqrt 与 cmath.sqrt 的分界线到底是什么？（运算域而非数值类型：math 拒绝复数参数、负数报 ValueError；cmath 全程复平面）
- 复数列表能 sorted 吗？（不能，TypeError；要排序必须显式定义投影键——库选择不定义武断字典序）

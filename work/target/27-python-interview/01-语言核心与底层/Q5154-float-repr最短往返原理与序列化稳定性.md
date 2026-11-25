---
title: "[Q5154] float repr 最短往返原理与序列化稳定性"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5154 · float repr 最短往返原理与序列化稳定性

难度：P6 ｜ 标签：float、repr、dtoa、序列化、round-trip

**问**：为什么 `repr(0.1)` 是 `0.1` 而不是 `0.1000000000000000055511151231257827`？"最短往返"（shortest round-trip）算法保证什么、不保证什么？这对你做"金额/坐标经 JSON 多跳传输不漂移"的设计有什么约束？

**答**：
结论：Python 3.1 起 repr/str 使用"最短十进制表示"算法（基于 David Gay 的 dtoa）：在所有能**唯一映射回同一个 IEEE-754 双精度值**的十进制串里取最短。它保证的是 `float(repr(x)) == x` 往返无损，**不保证**两个不同实现（如异构服务用不同格式化库）输出同串，也**不保证**人读的"短"等于数学上的精确值——`0.1` 只是二进制近似的最短标签。json.load/dump 默认走 float.__repr__，所以 Python↔Python 的 JSON 数值往返是稳定的；但一旦某跳经过会截断到固定位数的系统（如某些 Java/JS 序列化、Excel、 старый的 C 代码 `%.6f`），精度损失就固化进数据。

取舍：数值传输的三个层级——① 信任"最短往返"：全程 Python/标准 JSON，直接传 float（最省）；② 定点化：金额用整数分/Decimal+str 传（跨语言绝对稳）；③ 格式锁定：双方约定 `%.17g` 或 16 位有效数字（可互操作但可读性差）。多跳链路里只要有一跳不受你控制，就往 ② 收敛。

实战：对账类服务禁用 float 直传；坐标系/机器学习特征等容忍误差的用 ①；排查"两个服务算出的 JSON 数字字符串不一样"时，先确认各跳的格式化器版本（旧 CPython 2 的 repr 是 17 位全展开，混入会出长串）。

```python
import json, struct

# 1) 最短往返：repr 给出最短且 float() 回来相等的表示
x = 0.1
print("repr   :", repr(x))                       # 0.1
print("round-trip equal:", float(repr(x)) == x)
print("exact  :", x.hex(), "≠ 十进制 0.1（只是最短标签）")
print("17g 展开:", format(x, ".17g"))            # 0.10000000000000001

# 2) 为什么 0.2+0.1 != 0.3 但 repr(0.1+0.2) == '0.30000000000000004'：
#    最短往返必须"唯一指回这个双精度值"，0.3 指回的是另一个值
print("repr(0.1+0.2):", repr(0.1 + 0.2), " 回去相等?", float(repr(0.1 + 0.2)) == 0.1 + 0.2)

# 3) JSON 往返稳定性：默认 float_repr 驱动
s = json.dumps({"v": 0.1, "w": 1 / 3})
print("json dump :", s)
print("json load ==:", json.loads(s)["v"] == 0.1, json.loads(s)["w"] == 1 / 3)

# 4) 固定位数的一跳会固化误差（模拟 %.*f 的异构系统）
lossy = format(1 / 3, ".6f")
print("after a %.6f hop:", lossy, "->", float(lossy) == 1 / 3)

# 5) 双精度位级验证：struct 往返
bits = struct.pack(">d", x)
print("bit-level round trip:", struct.unpack(">d", bits)[0] == x)
```

**追问一**：最短表示为什么总是"唯一"的？——双精度有 53 位有效尾数，相邻两个可表示数之间隔了足够远，把 17 位有效数字空间按需收缩后，最短串与双精度值构成双射（这正是能"收缩"的前提）；若两个不同浮点数的最短串相同，往返就无法保证唯一，算法会在冲突时加长。

**追问二**：`json.dumps` 对特殊值（inf/nan）输出什么，跨语言风险在哪？——输出 `Infinity/NaN`（非标准 JSON，RFC 8259 不允许），严格解析器（Go/Java 多数库）会拒收；需要跨语言时先 `allow_nan=False` 打开校验，在生成端显式清洗。

## 背诵要点
- Python 3.1+ repr 用最短往返算法（David Gay dtoa）：保证 float(repr(x))==x，不保证跨实现输出一致。
- JSON 数值往返稳定的前提是每一跳都用最短往返；任何一跳固定位数（%.6f）误差即固化。
- 金额/对账走整数分或 Decimal 字符串；inf/nan 在 JSON 里非标准，跨语言先 allow_nan=False。

## 复盘追问
- 订单金额在 Python 服务与 Java 服务间经 JSON 传输出现 0.01 级别差异，如何定位到具体是哪一跳的格式化问题？（抓中间落库的原串比对位数；收敛为整数分传输）
- 为什么不能靠 `round(x, 2)` 解决多跳漂移？（round 仍是二进制近似且逐跳累积；只有定点化消除根因）

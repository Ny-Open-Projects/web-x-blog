---
title: "[Q5240] float.hex：十六进制浮点与精确往返"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5240 · float.hex：十六进制浮点与精确往返

难度：P6 ｜ 标签：float.hex、fromhex、精确往返、二进制表示、跨进程传输、调试、IEEE 754、C99 hexfloat

**问**：`float.hex()` 返回的 `0x1.999999999999ap-4` 是什么格式？"1.1 的十进制字符串"与"1.1 的 hex"哪个能精确还原？为什么 repr(0.1) 也能往返但 hex 更适合调试精度问题？hexfloat 与 `struct.pack` 二进制表示的关系是什么？跨进程/跨语言传输浮点为什么推荐 hex？

**答**：
结论：`float.hex()` 是 **C99 十六进制浮点字面量**（hexfloat）的 Python 实现：`0x1.999999999999ap-4` 分解为"1.9999...a（16 进制有效数字）× 2^-4（二进制指数）"——**每一位十六进制数对应 4 个二进制位，指数是 2 的幂**，所以这个表示**精确描述了 float 的 64 位二进制内容**，且 `float.fromhex(s)` 与 `s` 无损往返（这是 C99 `%a` 格式的家族）。与 repr 的对比：`repr(0.1)` 的 `'0.1'` 是**最短十进制往返表示**——它选了一个十进制串，其解析结果恰是这个 float，但串本身掩盖了"0.1 其实是 0x1.999999999999ap-4 = 0.1000000000000000055511151231257827021181583404541015625"的二进制真值；hex 则**直接暴露真值**。三件事只有 hex 干得了：①**诊断精度问题**：两个"看起来一样"的浮点数 hex 不同即可断言它们是不同的位模式（Q5234 的 nextafter 邻居用 hex 一眼可辨）；②**跨进程/跨语言精确传输**：hex 是位级精确的文本协议，不存在"printf 精度参数选错了"的问题——C 的 `%a`、Java 的 `Double.toHexString` 同族互认；③**与 struct 的桥梁**：`struct.pack('>d', x)` 的 8 字节就是 hex 描述的那 64 位（端序除外）。使用边界：hex 字符串不可读（人不会把 0x1.99... 当 0.1），所以它是**调试与协议层工具**，展示层永远用十进制。

取舍：a) 日志/调试浮点：hex 与 repr 同时打——hex 看位模式、repr 看语义值；b) 浮点跨进程传输（性能计数值、模型权重快照）：hex 或 struct 二进制，禁止 `str(x)`（str 与 repr 3.11+ 同为最短往返，可传但有解析方版本依赖——hex 是唯一位级契约）；c) 与 Decimal 的关系：`Decimal(x)` 从 float 构造得到的是**精确十进制展开**（可选 repr 的最短值），做货币换算要明确语义（Q538）；d) JSON 不支持 hexfloat，需要位级精确就要外挂字段（`{"v": 0.1, "hex": "0x1.9...p-4"}`）或改传 struct/base64；e) 性能：hex 编解码是 C 级小成本，但比二进制 struct 慢且膨胀 ~20 字节/值——高频通道用二进制，低频诊断用 hex。

实战：事故形态是"两个服务用 `str(float)` 传输风控分数，B 服务把字符串解析走的是 C 的 atof（精度规则不同），边界分数 0.9999999999999999 与 1.0 被混同——修复为协议层改传 float.hex 字符串（位级契约），展示层保留 repr，边界 case 单测用 nextafter 构造紧邻对并用 hex 断言位模式不同"。下面实测 hex 格式解析与三种传输方式的精确性对比。

```python
# float.hex: 十六进制浮点与精确往返
import json
import math
import struct

x = 0.1
h = x.hex()
print("[1] hexfloat 格式解剖: 0x1.999999999999ap-4 = 1.99...a * 2**-4")
print("    repr(0.1) =", repr(x), "(最短十进制往返表示)")
print("    (0.1).hex() =", h, "(位级精确的二进制-十六进制表示)")

print("[2] fromhex 无损往返, 且能暴露 repr 看不见的差异")
back = float.fromhex(h)
print("    fromhex(hex(x)) == x ->", back == x, "(位级往返恒等)")
a = 1.0
b = math.nextafter(1.0, math.inf)
print(f"    repr: {a!r} vs {b!r}", "(repr 相同! 最短往返表示一致)")
print(f"    hex : {a.hex()} vs {b.hex()}", "(hex 不同: 位模式不同, 一眼可辨)")

print("[3] 与 struct 的桥梁: hex 描述的就是那 64 位")
raw = struct.pack(">d", 0.1)
print("    struct.pack('>d', 0.1).hex() =", raw.hex(), "(大端 8 字节, 与 float.hex 同一内容不同排版)")

print("[4] 三种传输方式的精确性: repr/str vs hex vs struct")
samples = [0.1, 1 / 3, 1e300, 5e-324, float("inf")]
for v in samples:
    roundtrip_repr = float(repr(v)) if repr(v) not in ("inf", "nan") else v
    roundtrip_hex = float.fromhex(v.hex())
    print(f"    {v!r:>25}: repr 往返一致={roundtrip_repr == v}  hex 往返一致={roundtrip_hex == v}")

print("[5] hexfloat 的手算验证: 指数与尾数的关系")
import math
mant_bits = math.frexp(0.1)                          # 0.1 = m * 2**e, m in [0.5, 1)
print(f"    frexp(0.1) = {mant_bits} -> 0.1 = {mant_bits[0]:.4f} * 2**{mant_bits[1]}")
print("    hex 指数 -4 与 frexp 指数 -3 对应 (hex 归一化到 1.xxx 而不是 0.5.xxx)")

print("[6] JSON 无 hexfloat: 位级精确传输要外挂 hex 字段或二进制")
payload = {"score": 0.1, "score_hex": 0.1.hex()}
back_score = float.fromhex(json.loads(json.dumps(payload))["score_hex"])
print("    json 通道 + hex 字段往返一致:", back_score == 0.1)
print("[7] 工程纪律: 协议层浮点用 hex/struct 位级契约; 展示层 repr; 调试层两者并打")
```

**追问一**：repr 的"最短往返表示"是怎么选出来的？它与 hex 的本质差异在哪？—— repr（Python 3.1+，David Gay/Grisu 算法）的策略是：在所有能解析回这个 float 的十进制字符串中，取**字符数最少**的那个（平局取最接近真值的）。本质差异：repr 是"**挑一个十进制别名**"——0.1 的别名恰好长得像 0.1，但 1.1 的真值是 1.1000000000000000888178419700125232338905334472656250，别名 "1.1" 完全不显示这些信息；hex 是"**直写位模式**"——1.999999999999a × 2^-4 里的每一位十六进制数就是 IEEE 754 尾数的 4 个位，没有任何翻译层。推论：repr 往返依赖"解析器遵循同样的最短往返协议"（各家实现一致但这是约定），hex 往返依赖"IEEE 754 位语义"（标准强制）——诊断精度、跨语言协议这类"位级契约"场景必须 hex，人读场景必须 repr。这就是"两种表示服务两种契约"的设计分工。

**追问二**：`float.fromhex` 还能接受什么输入？"0x" 前缀可省吗？与 `int.fromhex`（bytes）的区别是什么？—— `float.fromhex` 接受完整 hexfloat 语法：`0x` 前缀可省（`fromhex('1.999999999999ap-4')` 合法）、允许符号与无穷（`fromhex('-0x1p-1074')`、`fromhex('inf')`？—— inf 不走 hex 路径，要用 `float('inf')`，fromhex 对 inf 报错）、指数 `p` 是二进制幂（p±n 表示 ×2^±n），与十进制指数 `e` 完全不同。两个易混点：①`float.fromhex("10")` 解析为 16.0（十六进制数值）不是十进制 10——它把输入当 hexfloat；②`int.fromhex("ff")` 是**另一族 API**——bytes 对象的十六进制解码（返回字节序列），与 float.hex（单个浮点的位模式文本）名字像、语义完全不同：`bytes.fromhex` 解码的是"字节串的十六进制文本"（Q5236），`float.fromhex` 解码的是"一个 IEEE 754 数的 hexfloat 字面量"。工程纪律：hexfloat 只在浮点位级场景使用，字节十六进制场景用 bytes.fromhex/hexlify，两者混用是隐蔽 bug 源。

## 背诵要点
- float.hex() = C99 hexfloat（尾数 16 进制 + 2 进制指数 p），位级精确，fromhex 无损往返；repr 是最短十进制别名（往返但不显真值）。
- 诊断/跨语言协议用 hex（位级契约），JSON 无 hexfloat 需外挂字段；struct.pack('>d') 的 8 字节就是 hex 描述的 64 位。
- float.fromhex 与 bytes.fromhex 是两族 API：前者解码单个浮点的 hexfloat，后者解码字节序列文本。

## 复盘追问
- 为什么调试浮点精度问题要打 hex 而不是 repr？（repr 是最短别名不显位模式；nextafter 邻居 repr 可能相同而 hex 可辨）
- repr 往返可靠为什么不能当位级传输协议？（往返依赖解析器同协议的约定；hex/struct 才是 IEEE 754 标准强制的位级契约）

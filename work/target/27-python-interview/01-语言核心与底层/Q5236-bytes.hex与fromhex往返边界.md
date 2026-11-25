---
title: "[Q5236] bytes.hex 与 fromhex：十六进制往返的解析边界"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5236 · bytes.hex 与 fromhex：十六进制往返的解析边界

难度：P5 ｜ 标签：bytes.hex、fromhex、十六进制、binascii、大小写、空白容忍、奇数长度、摘要展示

**问**：`bytes.hex()` 与 `bytes.fromhex()` 的往返语义是什么？大小写和分隔符怎么控制？`fromhex` 对空白的容忍规则是什么（3.7 vs 3.11 的差异）？奇数长度为什么必须报错？与 `binascii.hexlify/unhexlify` 的分工边界在哪？为什么摘要/密钥的展示层统一用 hex？

**答**：
结论：`bytes.hex(sep=None, bytes_per_sep=0)`（3.8+ 支持 sep）把字节序列编码为**小写**十六进制字符串，每个字节占两个字符、无损往返（`bytes.fromhex(b.hex()) == b` 恒成立）；`bytes.fromhex(s)` 解析十六进制字符串为字节，**大小写不敏感**（`"FF"` 与 `"ff"` 同解），**容忍空白**——空格会被跳过，3.11 起扩展到所有 ASCII 空白（含 `\n`、`\t`），使"复制粘贴换行分隔的摘要串"能直接解析。两条铁律：①**奇数长度必报 ValueError**（半个字节没有意义，`fromhex("abc")` 报 "non-hexadecimal number found"）；②**非法字符精确报错**并指明位置，解析失败是显式异常而不是静默错值——这是解析 API 的正确设计。与 binascii 的分工：`binascii.hexlify/unhexlify` 时代更早，输入输出是 **bytes**（hexlify(b"ff") 输出 b"6666" 这类），处理字符串还要 encode——新代码统一用 `bytes.hex/fromhex`，binascii 留给底层协议兼容。工程定位：hex 是字节序列的**展示/传输文本形态**——摘要（digest.hex()）、密钥与 IV、二进制协议调试日志、URL 里的二进制标识符都用它，因为 hex 无转义、无歧义、大小可控（2x 膨胀是代价）。

取舍：a) 只展示不传输：`.hex()`；b) 要插入分隔符便于人工核对：`b.hex(":")` 或 `b.hex(":", 2)`（bytes_per_sep 分组）；c) 反序列化外部输入：永远 `fromhex` + 异常处理，不要 `unhexlify` 后忽略错误路径；d) 更紧凑的文本编码（Base64 膨胀 4/3 vs hex 膨胀 2）：体积敏感的传输用 base64（Q5113），hex 胜在可人工比对；e) 大数据量编码：`hex()` 一次性物化 2x 字符串，流式场景按块编码再拼接，或换 base64 流式；f) 3.11 前后空白容忍差异意味着**同一份数据在 3.10 与 3.12 解析结果不同**（带换行的串前者崩后者过），跨版本部署的解析器要自己先 normalize。

实战：事故形态是"运维把生产摘要复制给排障脚本，粘贴时带了换行，3.10 环境下 `fromhex` 报 ValueError，同学手写 `replace("\n", "")` 修复——但另一处摘要带空格的写法在 3.12 升级后行为变化被掩盖；根治为解析入口统一 `"".join(s.split())` 显式 normalize 后再 `fromhex`，错误路径打印原始串与位置"。下面实测 hex 往返与解析边界。

```python
# bytes.hex 与 fromhex 往返
import binascii

data = bytes(range(16))
print("[1] hex 编码: 默认小写, 每字节 2 字符")
h = data.hex()
print("    data.hex() =", h)

print("[2] sep 与 bytes_per_sep: 可读性分组 (3.8+)")
print("    hex(':')       =", data[:8].hex(":"))
print("    hex(':', 2)    =", data[:8].hex(":", 2), "(每 2 字节插一次分隔)")
print("    hex('-', -4)   =", data.hex("-", -4), "(负数从右侧分组)")

print("[3] fromhex: 大小写不敏感, 往返无损")
print("    fromhex('0A0B') =", bytes.fromhex("0A0B"))
print("    fromhex(h) == data ->", bytes.fromhex(h) == data, "(round-trip 恒等)")

print("[4] 空白容忍: 空格全版本可跳; 3.11 起容忍全部 ASCII 空白")
print("    fromhex('aa  bb') =", bytes.fromhex("aa bb"))
print("    fromhex('aa\\nbb') =", bytes.fromhex("aa\nbb"), "(3.11+ 可直接解析换行分隔串)")

print("[5] 奇数长度与非法字符: 显式报错并指明位置")
for bad in ("abc", "zz", "aa c"):
    try:
        bytes.fromhex(bad)
    except ValueError as e:
        print(f"    fromhex({bad!r}) -> ValueError: {e}")

print("[6] 与 binascii 的分工: hexlify/unhexlify 进出都是 bytes, 新代码用 bytes.hex/fromhex")
print("    binascii.hexlify(b'AB') =", binascii.hexlify(b"AB"), "(bytes 进 bytes 出)")
print("    binascii.unhexlify('4142') =", binascii.unhexlify("4142"))

print("[7] 工程定位: 摘要/密钥/二进制日志的展示层统一 hex; 大传输量用 base64 (膨胀 4/3 vs 2x)")
import hashlib
print("    sha256 摘要展示:", hashlib.sha256(b"payload").hexdigest()[:32], "...")
print("[8] 跨版本纪律: 解析入口先 normalize 空白, 再 fromhex; 奇数长度是数据损坏的信号不是格式噪音")
```

**追问一**：为什么 `bytes.fromhex` 在 3.11 改成容忍所有 ASCII 空白？这类"解析器放宽"的风险是什么？—— 动机来自真实使用面：指纹/摘要串经常以换行或制表符分隔复制粘贴（证书指纹、git blob hash 的展示格式），3.7 只容忍空格的规则让每家都要手写 normalize。3.11 放宽到全部 ASCII 空白，让"从任意展示格式直接解析"成立。风险两面：①**跨版本行为分叉**——同一输入在 3.10 报错、3.12 通过，若有代码把"解析失败"当作"数据非法"的信号（如拒绝篡改串），升级后防线静默变松；②空白容忍不等于**内容校验放松**：非法 hex 字符仍然精确报错，"能过解析"永远不等价于"是合法摘要"——安全校验必须独立于解析器做（长度断言 + 常数时间比较，Q1829 家族）。记忆模型：解析器放宽只影响"格式容错"，不影响"内容有效性"，两者是不同层的契约。

**追问二**：hex、base64、base85 的膨胀率与选型矩阵是什么？为什么摘要展示界偏爱 hex？—— 膨胀率：hex 2.0x（每字节 2 字符）、base64 1.33x（每 3 字节 4 字符）、base85/z85 1.25x。选型维度是"人工可读性 × 体积 × 工具链"：hex 每字节与字符一一对应、大小写不敏感（多数场景）、`grep`/`diff`/眼睛比对都友好，摘要、指纹、密钥展示界统一 hex 是因为**可比对性**优先于体积；base64 胜在体积与二进制安全，用于 HTTP 头（Basic auth）、JWT 段、邮件附件——但大小写敏感且 `+/=` 在 URL 里需变体（urlsafe）；base85 体积最优但可读性最差，用于 git 二进制 diff、二进制补丁。另一层：hex 字符串在 JSON/URL/Cookie 里零转义成本，base64 的 `+ / =` 在 URL/表单里要 urlsafe 变体——**编码选择的隐性成本在下游工具链**，选型时把"谁会消费这串文本"想清楚。

## 背诵要点
- hex() 小写无损往返，hex(sep, bytes_per_sep) 可分组（3.8+）；fromhex 大小写不敏感，空白容忍（3.11 起含换行等全部 ASCII 空白）。
- 奇数长度/非法字符 ValueError 精确报错——解析失败是损坏信号；跨版本空白行为分叉要显式 normalize。
- binascii 进出是 bytes（旧 API）；新代码统一 bytes.hex/fromhex；展示层 hex（可比对），传输层 base64（体积）。

## 复盘追问
- 摘要串带换行为什么在不同 Python 版本解析结果不同？（3.11 起 fromhex 容忍全部 ASCII 空白；3.10 只容忍空格）
- hex 与 base64 怎么选？（人工比对优先 hex 2x 膨胀；体积与二进制安全优先 base64 1.33x，URL 场景用 urlsafe 变体）

---
title: [Q2343] bytes 与 str 的比较:两个不相通的世界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2343 · bytes 与 str 的比较:两个不相通的世界

> 难度:★★☆☆☆ | 标签:bytes, str, 编码

**问**:b"abc" 和 "abc" 相等吗?为什么 bytes 能当 dict key 却取不到 str 存的值?

**答**:bytes 与 str 是两种独立类型,任何比较都返回 False 而不是报错——b"\xe4\xb8\xad" == "中" 永远是 False,因为二者的 == 是跨类型直接判不等,不做任何隐式解码。哈希也遵循同一套字节/码点口径,所以 bytes 与其编码结果哈希不同,放进同一个 dict 是两个不同的键,互取不到。元素语义差别更大:索引 bytes 得到 int(b"abc"[0] 是 97),索引 str 得到单字符 str;迭代、in 检查同理,跨类型操作直接 TypeError。工程意义在于:类型边界就是编码边界,「先 decode 再处理、处理完再 encode」,绝不在比较与容器键上混用两种类型,能让一整类「看起来相等却查不到」的问题消失。

```python
# file: code/01_语言核心与底层/q2343_bytes_vs_str.py
"""bytes 与 str 的比较:永不相等、哈希不同、混排直接报错。"""

if __name__ == "__main__":
    text = "中文"
    data = text.encode("utf-8")
    print("bytes 形式:", data)
    print("与 str 比较:", data == text)
    print("decode 后相等:", data.decode("utf-8") == text)

    print("哈希不同:", hash(data) != hash(text))
    table = {text: "值"}
    try:
        table[data]
    except KeyError:
        print("bytes 键取不到 str 的值")

    print("b'abc' 索引得到:", b"abc"[0], type(b"abc"[0]).__name__)
    print("str 索引得到:", "abc"[0], type("abc"[0]).__name__)

    try:
        sorted(["a", b"a"])
    except TypeError as exc:
        print("混排:", exc)

    try:
        b"a" in "abc"
    except TypeError as exc:
        print("in 跨类型:", exc)
```

**追问**:1) 那 `b"abc" == b"abc"` 的比较成本是 O(1) 吗?——不是,是逐字节的 O(n) 最坏比较,先比长度;与 str 一样,等值检查在长字节串上并不免费。2) 两个世界的隔离规则?——bytes/str 之间 == 直接 False、不转换;拼接/切片/比较各自成体系;桥梁只有 encode/decode 一次转换,边界处理 errors 策略(Q1541)。3) 混用的典型报错?——TypeError: can't concat str to bytes;UnicodeDecodeError 在 decode 边界;f-string 混两者产生 b'...' 文本。4) 生产陷阱?——网络/文件层混用 bytes 与 str;在边界重复 encode/decode;按 str 假设切片(bytes 切片还是 bytes,len 是字节数不是字符数)。

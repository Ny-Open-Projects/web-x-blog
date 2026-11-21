---
title: [Q040] 字符串编码:Unicode 与 bytes
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q040 · 字符串编码:Unicode 与 bytes

> 难度:★★☆ | 标签:字符串, 编码

**问**:Python 3 的 str 和 bytes 什么关系?UnicodeEncodeError 和 UnicodeDecodeError 分别在哪发生?

**答**:str 是 Unicode 码点序列,bytes 是原始字节序列,两者转换必须显式指定编码:encode 编到 bytes,decode 回 str。对 str 调 encode 不存在的字符抛 UnicodeEncodeError;对错误字节流 decode 抛 UnicodeDecodeError。I/O 边界(文件、socket)永远操作 bytes,编码在边界处理;`open(..., encoding="utf-8")` 应显式指定,不依赖 locale 默认。处理脏数据可用 `errors="replace"` 或 `surrogateescape`。

```python
# file: code/01_语言核心与底层/q040_encoding.py
if __name__ == "__main__":
    s = "你好, Python"
    b = s.encode("utf-8")
    print(b, len(b), len(s))     # 字节数不等于字符数
    print(b.decode("utf-8"))

    try:
        b.decode("ascii")
    except UnicodeDecodeError as e:
        print("decode error:", e)

    print("emoji".encode("ascii", errors="replace"))
    raw = b"caf\xe9"
    print(raw.decode("latin-1"), "|", raw.decode("utf-8", errors="replace"))

    with open("/tmp/enc_demo.txt", "w", encoding="utf-8") as f:
        f.write(s)
    with open("/tmp/enc_demo.txt", "r", encoding="utf-8") as f:
        print(f.read())
```

**追问**:1) 为什么有时候 len(str) 和数据库长度对不上?——str 长度按码点统计,某些字符(组合符号、emoji)由多个码点组成,数据库可能按 UTF-8 字节或 grapheme 计数。2) 一个 emoji 的 len 是多少?——按码点计,基本平面 emoji len 为 1;但带组合符/肤色修饰的序列由多个码点组成,len 大于视觉长度,这正是与数据库按字节存储长度对不上的根源。3) 生产环境编码问题高发在哪?——Windows 默认 locale 编码的 `open()`/subprocess、日志文件、第三方接口;原则是 IO 边界显式 `encoding='utf-8'`(PEP 686 计划让 3.15 默认 UTF-8,但不能依赖)。

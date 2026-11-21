---
title: [Q1538] translate 与 maketrans:字符级批量映射的最快路径
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1538 · translate 与 maketrans:字符级批量映射的最快路径

> 难度:★★★★☆ | 标签:str, translate, 性能

**问**:批量做字符级替换(清洗、脱敏、ROT13),为什么 translate 比一串 replace 快?maketrans 的三种形态分别怎么用?

**答**:translate 按「字符级映射表」一次扫描完成全部替换,maketrans 是造表入口,三种形态:① maketrans(x, y) 等长字符串两两映射;② maketrans(x, y, z) 第三参是被删除字符集;③ maketrans(dict) 自由形态(单字符键 → 任意串或 None)。性能本质:translate 一遍 O(n),N 次 replace 是 N 遍扫描,清洗类任务的差距随替换项数量线性放大;bytes.translate 用 256 字节映射表更快,是协议清洗利器。限制:只能 1:1 映射或删除,变长替换(正则、多字符)是 re.sub 的领地。典型用途:脱敏掩码、ROT13、标点剥离、编码纠偏。

```python
# file: code/01_语言核心与底层/q1538_translate_maketrans.py
import string
import timeit

SANITIZE = str.maketrans("aeiou", "43107", string.punctuation)
SENSITIVE = str.maketrans({c: "*" for c in "password0123456789"})


def rot13_table():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    return str.maketrans(lower + upper,
                         lower[13:] + lower[:13] + upper[13:] + upper[:13])


def clean_with_replace(text):
    """反模式:一串 replace,每个替换都全文扫描一遍。"""
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text.translate(str.maketrans("aeiou", "43107"))


if __name__ == "__main__":
    raw = "Hello, World! Email: user@example.com 2026-11-05"
    print("sanitize :", raw.translate(SANITIZE))
    print("mask     :", "password: 42".translate(SENSITIVE))
    print("rot13    :", "The Quick Brown Fox".translate(rot13_table()))

    text = raw * 400
    n = 30
    t_translate = timeit.timeit(lambda: text.translate(SANITIZE), number=n)
    t_replace = timeit.timeit(lambda: clean_with_replace(text), number=n)
    print("translate    :", round(t_translate * 1000 / n, 3), "ms per run")
    print("replace chain:", round(t_replace * 1000 / n, 3), "ms per run")

    # bytes.translate:256 字节映射表,协议清洗的常用工具
    b = b"hello\x00world"
    print("bytes    :", b.translate(bytes.maketrans(b"lo", b"10"),
                                   delete=b"\x00"))
```

**追问**:1) translate 能做大小写折叠吗?——能映射但不是 casefold 的语义(ß、İ 这类多字符折叠它管不了);语言级折叠用 str.casefold,translate 只管字符级 1:1。2) 为什么它最快?——C 层单遍扫描查映射表,一次完成替换与删除;str.replace 链每条都要全文扫一遍;循环调用 str.replace 的成本是线性叠加的。3) maketrans 的语义?——字符 1:1 映射,None 表示删除;不支持多字符映射(那是 re.sub 的领地);映射表可复用(模块级构建一次)。4) 生产陷阱?——多字符替换误用 translate 静默漏替换;重复构建 maketrans 表;忽略 translate 返回新串(原串不变);清洗管道顺序不当(先删后映射 vs 先映射后删)。

---
title: [Q491] Unicode 规范化:NFC/NFD 与相等性
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q491 · Unicode 规范化:NFC/NFD 与相等性

> 难度:★★★★ | 标签:Unicode, 字符串

**问**:两个「看起来一样」的字符串为什么不相等?比较用户输入的字符串前应该做什么?

**答**:Unicode 允许同一个字形有两种编码:预组合(é 一个码点)与分解(e + 组合重音两个码点),用户输入来源不同(键盘、剪贴板、macOS 文件名)会混用两种形式,直接 == 会假阴性。处理规则:在系统边界统一 `unicodedata.normalize("NFC", s)`(存储/比较用 NFC 最普遍),比较用 normalize 后的值;文件名场景 macOS 是 NFD。is_normalized 可避免重复规范化。除规范化外,大小写折叠用 casefold()(比 lower 更激进,处理德语 ß)才是无差别比较的正解。

```python
# file: code/01_语言核心与底层/q491_unicode_normalization.py
import unicodedata

s1 = "caf\u00e9"          # 预组合:é 是单个码点
s2 = "cafe\u0301"         # 分解:e + 组合重音两个码点

if __name__ == "__main__":
    print("codepoints s1:", [hex(ord(c)) for c in s1])
    print("codepoints s2:", [hex(ord(c)) for c in s2])
    print("direct equality:", s1 == s2)

    n1 = unicodedata.normalize("NFC", s1)
    n2 = unicodedata.normalize("NFC", s2)
    print("NFC equality:", n1 == n2, "len:", len(n1))

    print("NFD len:", len(unicodedata.normalize("NFD", s1)))
    print("already NFC:", unicodedata.is_normalized("NFC", n1))
    print("casefold:", "STRASSE".casefold() == "straße".casefold())
```

**追问**:1) NFC 和 NFD 该选哪个存库?——统一即可,主流选 NFC(体积小、兼容多数输入);关键是「入口归一化一次」,而不是在每次比较处反复转换。2) 为什么「看起来一样」的字符串不相等?——同一字形有组合字符与预合成字符两种编码(macOS 文件系统产 NFD、网页输入多为 NFC),== 比较码点序列,必须 unicodedata.normalize 后再比。3) 四种 form 的底层差异?——NFD 按规范分解、NFC 分解后重组,NFKC/NFKD 额外做兼容分解(上标²→2、连字);规范化按 UAX #15 实现,规范等价只在 normalize 后才体现。4) 生产陷阱?——用户名/标签因规范化形式不同绕过唯一约束;NFKC 误用于「清洗」用户输入会改变语义;数据库层校验不了规范化,必须在应用入口统一。

---
title: [Q2142] URL 构造的编码坑:quote 与 urlencode 的边界
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2142 · URL 构造的编码坑:quote 与 urlencode 的边界

> 难度:★★☆ | 标签:urlencode, quote, 编码

**问**:拼 URL 时参数里的空格、&、中文该怎么编码?最容易踩的坑是什么?

**答**:query 参数交给 urlencode,路径片段交给 quote;最典型的坑是手工拼接——& 和空格直接改写 URL 结构,实测坏 URL 的 query 被解析成完全不同的键值。

- urlencode 把空格变 +、保留字转义,parse_qs 完整还原;

- quote 默认放行 /,路径场景要 safe='' 才会把斜杠也转义;

+ 与 %20 在 query 里同义、在 path 里语义不同,不能乱混;

- 已编码串再 quote 会二次编码成 %252F,是线上最常见的编码事故。

```python
# file: code/02_并发与网络工程/q2142_url_encode_traps.py
# -*- coding: utf-8 -*-
"""URL 构造的编码坑: quote 与 urlencode 的边界。

- query 参数用 urlencode: 空格变 +, 保留字被转义, 解析侧 parse_qs 还原;
- path 片段用 quote: / 有语义不能转, safe 参数决定放行谁;
- 两大坑: 已编码串被二次编码, + 与 %20 在 path 与 query 语义不同。
"""
from urllib.parse import (urlencode, parse_qs, quote, quote_plus,
                          unquote, unquote_plus, urlunsplit, urlsplit)


def show(tag, value):
    print("%-28s -> %s" % (tag, value))


def main():
    params = {"q": "a b&c=d", "tag": "中文#1"}
    qs = urlencode(params)
    show("urlencode(参数)", qs)
    show("parse_qs 还原", parse_qs(qs))

    path_seg = "目录/文件 名.txt"
    show("quote(path, 默认 safe=/)", quote(path_seg))
    show("quote(path, safe='')", quote(path_seg, safe=""))
    show("quote_plus(空格变+)", quote_plus(path_seg))

    show("已编码再编码", quote("%2F"))          # %252F: 二次编码事故
    show("unquote 一次", unquote("%2F"))
    show("unquote_plus 吃掉+", unquote_plus("a+b"))

    base = "https://api.example.com/search"
    url = urlunsplit(("https", "api.example.com",
                      "/search", qs, ""))
    show("拼出的完整 URL", url)
    parts = urlsplit(url)
    show("回读 query", parse_qs(parts.query))

    # 常见事故: 手工拼字符串, & 和空格直接破坏结构
    broken = base + "?q=" + params["q"]
    show("手工拼接(坏)", broken)
    show("坏 URL 的 query 解析", parse_qs(urlsplit(broken).query))
    print("结论: 参数交给 urlencode, 路径交给 quote, 禁止手工拼接")


if __name__ == "__main__":
    main()
```

**追问**:1) quote 和 quote_plus 差在哪?——前者空格变 %20、用于 path,后者变 +、用于 query,选错只是表现差异,埋雷在后端解析。2) 为什么中文会变成 %E4%B8%AD?——UTF-8 字节逐字节百分号编码,解析侧按 UTF-8 还原,链路两端必须约定同一编码。3) 二次编码的完整事故链?——已编码串(%2F)再 quote→%252F;后端解码一次得 %2F(字面量),再解码才得 /——两次解码语义不同;防线:编码一次且在「最终组装」时做,内部表示保持未编码;parse_qs/unquote 只在边界调用。4) + 与 %20 的语义分裂怎么处理?——query 里 + =空格(x-www-form-urlencoded 惯例),path 里 + 是字面加号;quote(空格→%20) 用于 path,quote_plus(+ ) 用于 query;跨场景混用就是「加号变空格」事故——「位置决定编码」。5) 生产陷阱?——手工拼 URL(&/空格改写结构);safe 默认放行 / (path 片段含斜杠穿越);中文编码两端不一致(GBK vs UTF-8 乱码);把已编码值塞进 urlencode(二次编码);fragment(#后)被参与签名(URL 签名把 # 后内容算进去或漏掉)。

---

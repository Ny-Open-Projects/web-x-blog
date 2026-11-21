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

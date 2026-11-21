---
title: [Q1539] partition vs split:单刀切分的语义与选型
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1539 · partition vs split:单刀切分的语义与选型

> 难度:★★☆☆☆ | 标签:str, 解析, 字符串

**问**:解析 "host:port" 这类单分隔符字符串,partition 和 split 选哪个?它们语义差在哪?

**答**:partition(sep) 沿第一个分隔符切成 (head, sep, tail) 三元组,sep 不存在时返回 (原串, '', ''),返回形状恒定——解构不需要判长度、不写防御分支;rpartition 从右往左找第一刀,扩展名、路径尾段这类「从右解析」必须用它。split 更通用但形状不定:无分隔符时返回单元素列表,多次出现时全切,maxsplit 控制刀数。细节差异常考:split() 无参按任意空白切并压缩连续空白,split(' ') 只按单个空格切、连续空格产生空串。选型:「恰好切一刀」的键值对、协议行用 partition;多字段、去空白、批量切分用 split。

```python
# file: code/01_语言核心与底层/q1539_partition_vs_split.py


def parse_endpoint(text):
    """partition:返回形状恒定,解构不用判长度。"""
    host, sep, port = text.partition(":")
    return host, int(port) if sep and port.isdigit() else None


if __name__ == "__main__":
    for raw in ("db.internal:5432", "localhost", ":9999"):
        print(raw, "->", parse_endpoint(raw))

    # 扩展名要从右切:文件名里可能有多个点
    for path in ("archive.tar.gz", "README", ".hidden"):
        stem, dot, ext = path.rpartition(".")
        print(path, "-> stem:", stem or path, "ext:", ext if dot else "")

    # split 的两个细节:无分隔符 vs 空白压缩
    print("split ':' no sep :", "localhost".split(":"))
    print("split() 压缩空白 :", "a  b\tc\n d".split())
    print("split(' ') 不压缩:", "a  b".split(" "))
    print("maxsplit=1       :", "k=v=more".split("=", 1))
    print("partition 一刀   :", "k=v=more".partition("="))
```

**追问**:1) partition 对多字节分隔符呢?——sep 可以是任意长字符串,同样只切第一刀;rpartition 找最后一刀,「从右解析」场景必须用它。2) partition 与 split 的选型?——单刀用 partition:恒返回 3 元组(找不到 sep 时是 (原串, "", "")),无需判断列表长度;split 适合多段与 maxsplit 语义;扩展名分离 rpartition(".") 才对(文件名里可能有点)。3) 解析链组合?——partition 返回 (before, sep, after),after 继续下一刀,比 split(":", 1) 后再拼更清晰;不依赖分隔符出现与否的分支。4) 生产陷阱?——split 结果空列表/长度不定导致 IndexError;从左 partition 处理扩展名/路径把第一个点当分隔;忘记 partition 找不到时 sep 是空串。

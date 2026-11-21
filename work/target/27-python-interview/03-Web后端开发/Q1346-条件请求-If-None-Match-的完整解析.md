---
title: [Q1346] 条件请求:If-None-Match 的完整解析
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1346 · 条件请求:If-None-Match 的完整解析

> 难度:★★★ | 标签:HTTP 缓存, 接口设计

**问**:除了最简单的单 ETag 比对,If-None-Match 还有哪些合法形态?中间件里怎么把解析做对?

**答**:`If-None-Match` 可以是逗号分隔的多个实体标签、带 `W/` 前缀的弱标签,或 `*`(表示任意实体存在即命中)。判定要用**弱比较**(忽略 `W/` 前缀只比标签本体),且客户端发来的列表必须逐项解析而不是整个字符串相等——这是新手中间件最常见的 bug。命中就返回 304 并回带 ETag 与缓存指令,不命中才真正生成响应体。把这套解析收敛成纯函数,单测覆盖 `*`、多标签、弱标签三种形态,中间件只做组装。

```python
# file: code/03_Web后端开发/q1346_conditional_request.py
"""条件请求:If-None-Match 的解析与 304 判定(纯标准库)。"""


def parse_if_none_match(value):
    """解析 If-None-Match,返回 [(weak: bool, tag: str)];* 表示任意实体。"""
    if not value:
        return []
    value = value.strip()
    if value == "*":
        return [(False, "*")]
    tags = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        weak = part.startswith("W/")
        if weak:
            part = part[2:]
        tags.append((weak, part.strip()))
    return tags


def not_modified(etag, if_none_match):
    """按 RFC 7232 的弱比较判定:命中返回 True,服务端应回 304。"""
    tags = parse_if_none_match(if_none_match)
    if not tags:
        return False
    if any(tag == "*" for _, tag in tags):
        return True
    ours = etag[2:] if etag.startswith("W/") else etag
    return any(tag == ours for _, tag in tags)


resource_etag = '"v7"'
print("单标签命中:", not_modified(resource_etag, '"v7"'))
print("多标签命中:", not_modified(resource_etag, '"v6", "v7"'))
print("星号命中:", not_modified(resource_etag, "*"))
print("弱标签命中:", not_modified(resource_etag, 'W/"v7"'))
print("不命中:", not_modified(resource_etag, '"v8"'))
print("空头不命中:", not_modified(resource_etag, None))
```

**追问**:
- If-None-Match 和 If-Modified-Since 同时带时听谁的?——规范规定 If-None-Match 优先,只有前者缺席才看日期。
- 304 能省多少?——省掉整个响应体的传输与序列化,CPU 只剩指纹计算,大响应收益最明显。
